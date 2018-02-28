# Parse v1

Este parser o analizador está pensado para leer la información de los gigantescos archivos de texto que proporcionan los problemas de Google Hash, interpretándola y cargándola en una estructura de objetos de python.

Para ello propone la definición de un conjunto de reglas que "mapearán" todos los datos del archivo de texto con clases de python.

## Puesta en funcionamiento 
Bajar el fichero [gcode17.py](gcode17.py) e importar la función `parse`:
```python
from gcode17 import parse
```
La función `parse` recibe la ruta del fichero de entrada, la estructura del fichero, y un diccionario de funciones (utilizar la función `globals()`):
```python
problema = parse(path, struct, globals())
```
Y tendremos que recoger el resultado de esa llamada en una variable (en este caso __problema__), que va a contener toda la estructura que definamos cargada con la información parseada.

En ese archivo __.py__ en el que hemos importado __gcode17.py__ deberemos definir las **clases de python** (ver más adelante los manejadores), que no debemos confundir con las **clases de las reglas** que no es lo mismo.

## Definición de la estructura del fichero
La estructura se define en una cadena de texto, donde cada línea de la estructura contiene una **regla**. Las reglas tienen el siguiente aspecto:
```
Clase = literal1 Tipo1 Tipo2 otro literal Tipo3 -> Clase2 -> Clase3 -> Clase4 | Manejador
```
Todas las reglas empiezan definiendo su clase (que puede verse como el "Tipo" o "Nombre" de la regla) seguido de un `=`.

Luego se pueden definir `literales`, `tipos` y `clases`.

Y finalmente el manejador después del `|`.

El orden de evaluación de estas reglas es de izquierda a derecha y desde menos a más profundidad.

La primera regla del programa debe ser de la clase `Main`, por ejemplo:
```
Main = foo Int Int -> Albondiga -> Macarron | Problem
```
Esta es una regla de la **clase** `Main`. Después del símbolo igual `=` se especifica qué debe contener la línea a ser parseada. En este caso, la clase `Main` debe encontrarse con una línea que contenga literalmente la palabra `foo` seguida de dos enteros que son uno de los tipos soportados. 

Los **tipos** implementados son: 

* entero `Int`
* real `Float`
* cadena `String`
* lista de enteros `*Int`
* lista de reales `*Float`
* lista de cadenas `*String`

### Uso de las clases de las reglas

Opcionalmente, en la parte derecha (o incluso intercalando con `tipos` y `literales`) de la regla pueden aparecer una o varias `-> ClaseX`, que indican que la línea que se ha parseado debe ir seguida de otra línea que se parsee con una regla de la **clase** `ClaseX`. En nuestro ejemplo, estamos diciendo que la primera linea tiene dos enteros, y que le siguen una linea de la **clase** `Albondiga` y una linea de la **clase** `Macarron`. Hay que añadir una regla para cada clase:
```
Main = foo Int Int -> Albondiga -> Macarron | Problem
Albondiga = Int | Albon
Macarron = Float *Int | Mac
```
Por ejemplo, para el siguiente fichero de entrada:
```
foo 1 2
3
3.2 4 2 5 2 6 2
```
Empezamos parseando en la **linea 1**, y siempre se empieza a parsear con una regla de la **clase** `Main`. Vemos que la primera linea se ajusta a la definición de `Main = foo Int Int`, por lo tanto leemos el `1` y el `2`. Ahora la regla de `Main` nos dice que lo que sigue (`-> Albondiga`) se parsea con una regla de la **clase** `Albondiga`.

Estamos en la **linea 2** y se debe parsear con una regla de la **clase** `Albondiga`, para la cual solo hemos puesto una regla: `Albondiga = Int | Albon`. Como la segunda línea sólo contiene un entero, se ajusta a la definición y podemos leer el `3`. Como la regla de `Albondiga` no nos dice que después vaya algo (no tiene ninguna flecha `->`) ¡hemos leído una albondiga completa! Así que devolvemos a la regla que llamó a la albondiga el resultado `Albon(3)`, y seguimos.

Estamos en la **linea 3** y ahora `Main` nos dice que viene un macarrón (`-> Macarron`). La única regla de la **clase** `Macarron` es `Macarron = Float *Int | Mac`, y vemos que encaja con la tercera linea. Por lo tanto leemos el real `3.2` y la lista de enteros `[4,2,5,2,6,2]`, y devolvemos a main el resultado `Mac(3.2,[4,2,5,2,6,2])`.

La regla de la clase `Main` ha terminado, y el fichero también, así que devolvemos como resultado `Problem(1,2,Albon(3),Mac(3.2,[4,2,5,2,6,2]))`.

### Paso de argumentos a las clases

Las **clases** especificadas tras una flecha `->` admiten argumentos, encerrados entre paréntesis y separados por comas:

```
Clase = ... -> Clase2(arg1,arg2) -> Clase3(arg1) -> Clase4
```

Estos argumentos pueden ser números literales `n`, el n-ésimo dato **ya parseado** por la regla actual `n@`, o el n-ésimo argumento recibido por la regla actual `n#`. Por ejemplo:
```
Main = Int Int -> Block(2@) | Problem
Block = -> 1#Line
Line = Int Int | Line
```

El segundo dato leído por ```Main``` se pasa como primer argumento de ```Block```. Luego, en la segunda línea, este primer argumento es usado para indicar el número de lineas de la clase ```Line``` a parsear (se explica en la siguiente sección).

Nota: Hay que tener en cuenta el orden de evaluación, y no referenciar datos no parseados aún.

### Modificadores de las clases

Las **clases** especificadas tras una flecha `->` admiten los siguientes modificadores:

* `n@Clase` indica que tiene que leer el número de lineas especificadas por el **n-ésimo** dato parseado en la regla actual. Por ejemplo, `1@Clase` indica que a continuación hay que leer tantas lineas aplicando las reglas de la **clase** `Clase` como indique el **n-ésimo** dato parseado en la regla actual.
* `n#Clase` indica que tiene que leer el número de lineas especificadas por el **n-ésimo** argumento de la regla actual. Por ejemplo, `1#Clase` indica que a continuación hay que leer tantas lineas aplicando las reglas de la **clase** `Clase` como indique el **n-ésimo** argumento de la regla actual.
* `nClase` indica que a continuación hay que leer tantas lineas con la **clase** `Clase` como indique el número **n**. Por ejemplo, `3Clase` indica que hay que leer las **3** líneas siguientes con reglas de la **clase** `Clase`.
* `*Clase` indica que tiene que parsear tantas líneas siguientes como pueda con reglas de la **clase** `Clase`.

Nota: La regla actual es la regla en la que esta escrita la invocación `->` a la clase.

En el ejemplo siguiente estamos indicando que se van a evaluar tantas líneas con la clase `Block` como indique el segundo Int.

```
Main = Int Int -> 1@Block | Problem
Block = -> Int Int | Block
```

### Ajuste de patrones

Las **clases** aceptan varias reglas. Una linea a parsear con una clase, se parseará con la primera regla de dicha clase con la que pueda ajustarse:
```
Main = foo Int *Int -> 1@Command -> End  | Problem
Command = circle Int Int Float | Circle
Command = rect Int Int Int Int | Rect
End = Int
```
En el ejemplo, la clase Command tiene dos reglas, siempre que se intente aplicar Command se comprobará si la primera regla 'encaja' con lo encontrado, sino
se recurrirá a la segunda (y a las siguientes sucesivamente si las hubiese).

### Dejar de leer

Para dejar de leer el fichero prematuramente, se puede utilizar la clase punto `.`:
```
Main = foo Int *Int -> 1@Command -> .  | Problem
Command = circle Int Int Float | Circle
Command = rect Int Int Int Int | Rect
```
En el ejemplo, si hubiese más lineas despues de las líneas interpretadas con la clase Command se ignorarían y el parser devolvería lo que tuviese.

### El manejador

Al final de las reglas se suele colocar la barra vertical `|` para indicar a continuación el manejador. El manejador puede ser una **clase o una función de python**.

Si es una **función de python**, se utilizará para hacer un tratamiento de los datos parseados de la linea (que recibirá como parámetros) y nos quedaremos con lo que retorne, es decir, se aplicará esa función a los datos parseados.

Si es una **clase de python** se usará para crear instancias (objetos) derivados de la regla, donde la instancia recibirá como parámetros del \_\_init\_\_ los datos parseados de la regla y como retorno nos quedamos con la instancia.

El manejador es obligatorio si existen más de un dato parseado. Si sólo es uno y no se especifica, se utiliza la función identidad ``` lambda x: x ``` que nos devolvería el dato en crudo (p.ej. sin ser un objeto de otra clase).

Estas clases o funciones se definen en el archivo __.py__ en el que hemos importado __gcode17.py__ (ver "Puesta en funcionamiento" al principio)

## Ejemplos

1. [`metahash/parse/clases.py`](clases.py) con el fichero de entrada [redundancy.in](redundancy.in)
2. [`metahash/parse/problema.py`](problema.py) con el fichero de entrada [in.txt](in.txt)