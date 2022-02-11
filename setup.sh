#!/bin/bash

docker-compose stop

docker-compose down --remove-orphans

docker-compose build

echo "Starting DB. Please wait..."
docker-compose up --build -d db

docker-compose up first-setup