# Parse
## Carga 
Bajar el fichero [gcode17.py](gcode17.py) e importar la función `parse`:
```python
from gcode17 import parse
```
La función `parse` recibe la ruta del fichero de entrada, la estructura del fichero, y un diccionario de funciones (utilizar la función `globals()`):
```python
parse(path, struct, globals())
```

## Definición de la estructura del fichero
La estructura se define en una cadena de texto, donde cada línea de la estructura contiene una regla. Las reglas tienen el siguiente aspecto:
```
Clase = literal1 Tipo1 Tipo2 otro literal Tipo3 -> Clase2 -> Clase3 -> Clase4 | Manejador
```
La primera regla del programa debe ser de la clase `Main`, por ejemplo:
```
Main = foo Int Int -> Albondiga -> Macarron | Problem
```
Esta es una regla de la **clase** `Main`. Después del símbolo igual `=` se especifica qué debe contener la línea a ser parseada. En este caso, la clase `Main` debe encontrarse con una línea que contenga literalmente la palabra `foo` seguida de dos enteros. Los **tipos** implementados son entero `Int`, real `Float`, cadenas `String`, lista de enteros `*Int`, lista de reales `*Float`, y lista de cadenas `*String`.

Opcionalmente, en la parte derecha de la regla pueden aparecer una o varias `-> ClaseX`, que indican que la línea que se ha parseado debe ir seguida de otra línea que se parsee con una regla de la **clase** `ClaseX`. En nuestro ejemplo, estamos diciendo que la primera linea tiene dos enteros, y que le siguen una linea de la **clase** `Albondiga` y una linea de la **clase** `Macarron`. Añadiremos una regla para cada clase:
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

Las **clases** especificadas tras una flecha `->` admiten los siguientes modificadores:

* `n@Clase` indica que tiene que leer el número de lineas especificadas por el **n-ésimo** dato parseado en la línea actual. Por ejemplo, `1@Clase` indica que a continuación hay que leer tantas lineas con reglas de la **clase** `Clase` como indique el **n-ésimo** argumento parseado en la linea actual.
* `nClase` indica que a continuación hay que leer tantas lineas con la **clase** `Clase` como indique el número **n**. Por ejemplo, `3Clase` indica que hay que leer las **3** líneas siguientes con reglas de la **clase** `Clase`.
* `*Clase` indica que tiene que parsear tantas líneas sigueintes como pueda con reglas de la **clase** `Clase`.

Las **clases** aceptan varias reglas. Una linea a parsear con uan clase, se parseará con la priemra regla de dicha clase con la que pueda ajustarse:
```
Main = foo Int *Int -> 1@Command -> End  | Problem
Command = circle Int Int Float | Circle
Command = rect Int Int Int Int | Rect
End = Int
```
Si se omite la función que recibe los argumentos, se utilizará la función identidad, devolviendo lo mismo que se haya leido. Sólo debería omitirse cuando sólo haya un único argumento, como en el caso de `End = Int`.

## Ejemplos

### Ñiaaa 1

### Ñiaaa 2

### Ñiaaa 3
