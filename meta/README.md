# Meta algoritmo genético v1

## Pasos para implementar una solución

En un archivo __.py__:

1. Importar las clases necesarias
    ```python
    from genetico import Individuo,Gen,Pool
    ```
2. Definir las clases que harán de `Individuo` y `Gen` heredando las clases `Individuo` y `Gen`
    ```python
    class Caracter(Gen):
        pass

    class Cadena(Individuo):
        pass

    ```
3. Implementar los métodos `__init__` en la clase que herede de `Gen` y `evaluar` en la que herede de `Individuo`. En `__init__` hay que inicializar el gen, normalmente con una configuración aleatoria. En `evaluar` hay que calcular la puntuación (como es de bueno) del individuo y asignarla a la variable `self.score`.
    ```python
    class Caracter(Gen):
        def __init__(self):
            # Inicializar el gen

    class Cadena(Individuo):
        def evaluar(self):
            self.score = ??? # Asignar la puntuación

    ```
4. Adicionalmente se debe implementar en la clase que herede de `Individuo` la funcion `exportar(self)` que se invocará con el mejor individuo encontrado al final, normalmente para presentar la solución (por pantalla, por fichero...)
    ```python
    class Cadena(Individuo):
        def evaluar(self):
            self.score = ???

        def exportar(self):
            pass

    ```
5. Finalmente incluir una clase con la configuración y la llamada a ejecución. Se puede copiar y adaptar el siguiente código:
    ```python
    class GENETIC_CONFIG:
        gencls = Caracter # Clase Gen
        individuocls = Cadena # Clase Individuo
        tpob = 16 # Tamaño de la población (Numero par plz)
        maxgenest = 5000 # Número máximo de generaciones estancadas
        pmutacion = 0.1 # Probabilidad de mutacion
        pcruze = 0.5 # Probabilidad de cruze
        ngenes = 12 # Numero genes


    pool = Pool(GENETIC_CONFIG())
    pool.doSearch()
    ```
Y a funcionar.

## Ejemplo

Evolucionar una cadena de texto: [`ghello.py`](metahash/meta/ghello.py)