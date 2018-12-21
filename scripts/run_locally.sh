#!/bin/bash
eval $(docker-machine env -u)d

docker-compose -f docker-compose-dev.yml up -d --build
docker-compose -f docker-compose-dev.yml run users python manage.py recreate-db
docker-compose -f docker-compose-dev.yml run users python manage.py seed-db
