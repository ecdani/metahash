FROM php:7.4-cli

RUN apt-get update
RUN apt-get install curl
RUN curl https://getcomposer.org/installer -o composer-setup.php \
  && php composer-setup.php \
  && mv composer.phar /usr/bin/composer

WORKDIR /project
