Desde la carpeta docker

Generación del contenedor (solo un vez tras el clonado)
- docker-compose build php

Generación del autoload (solo una vez tras el clonado)
- docker-compose run php composer install

Para ejecutar el proyecto
- docker-compose run php
