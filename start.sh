#!/bin/bash
docker-compose stop

docker-compose down --remove-orphans

docker-compose build --remove-orphans

docker-compose up --build django-dev --remove-orphans