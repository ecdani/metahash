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
La estructura se definen en una cadena de texto, donde cada línea contiene una producción. La primera producción del programa debe empezar por el no terminal `Main`:
```
Main = foo Int *Int -> 1@Command -> End  | Problem
```
En la parte derecha, `foo Int *Int` indica que la línea debe contener literalmente `foo` seguido de un entero, seguido de una lista de enteros. Todo ello en la misma línea. Los tipos implementados son `Int`, `Float`, `String`, o sus versiones precedidas por un asterisco, para indicar que son una lista indefinida.

El símbolo `->` indica que la siguiente línea debe ajustar con una producción de dicho no terminal. Estos no terminales admiten los siguientes modificadores:

* `n@`NoTerminal indica que tiene que leer el número de lineas especificadas por el **n-ésimo** argumento de la línea actual. Por ejemplo, `1@Command` indica que hay que leer el número de comandos especificado por el entero que se lee tras `foo`, que es el primer argumento leído.
* `n`NoTerminal indica que tiene que leer el número de lineas especificadas por **n**. Por ejemplo, `3Command` indica que hay que leer 3 comandos.
* `*`NoTerminal indica que tiene que leer un número indefinido de líneas.

Finalmente, lo que se encuentra tras la barra `|` indica el nombre de la función que atenderá los parámetros. Si el nombre es de una clase, se pasarán los argumentos al constructor y se obtendrá una instancia de dicha clase. Nótese que la regla `Main`, por ejemplo, recogerá un entero, una lista de enteros, una lista de lo que devuelvan los no terminales `Command` seguido de lo que devuelva el no terminal `End`, por lo que la función `Problem` recibirá 4 parámetros.

Los no terminales aceptan varias definiciones. La linea se parseará con la primera definición que se ajuste:
```
Main = foo Int *Int -> 1@Command -> End  | Problem
Command = circle Int Int Float | Circle
Command = rect Int Int Int Int | Rect
End = Int
```
Si se omite la función que recibir los argumentos, se utilizar la función identidad, devolviendo lo mismo que reciba. Sólo debería omitirse cuando sólo haya un único argumento, como en el caso de `End = Int`.

En la parte derecha, antes de la primera flecha `->` sólo se puede usar texto literal o los tipos mencionados anteriormente. Después de cada flecha, sólo se puede indicar otro no terminal, con o sin modificadores. Se puede terminar la lectura del fichero prematuramente si tras una flecha ponemos un punto, `End = Int -> .`.

## Ejemplos

### Ñiaaa 1

### Ñiaaa 2
