#!/bin/bash

docker-compose build

docker-compose stop

docker-compose down --remove-orphans

echo "Starting DB. Please wait..."
docker-compose up --build -d db

docker-compose up setup