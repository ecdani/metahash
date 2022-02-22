# Problema GHash 2022

## Requisitos

Docker, docker-compose y sh

## Ejecución

- Pegar los archivos de entrada en la carpeta `input`
- Ejecutar `./run` en la terminal

## Estructura del proyecto

En principio solo hace falta modificar los 3 archivos de la carpeta `src` (el bucle que lee los archivos de la carpeta está en `main.js`):

- **parser.js:** Se encarga de leer el archivos de entrada (aquí habrá que devolver los objetos con los datos)
- **problem.js:** Se encarga de resolver el problema como tal. Obtiene los datos de `parser.js` y le pasa los resultados a `writer.js`
- **writer.js:** Se encarga de escribir los resultados en el archivos de salida
