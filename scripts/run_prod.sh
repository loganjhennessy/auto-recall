#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS=~/Credentials/remember-it-compute-engine.json
eval $(docker-machine env auto-recall-prod)
docker-machine start auto-recall-prod

docker-compose -f docker-compose-prod.yml up -d --build
docker-compose -f docker-compose-prod.yml run users python manage.py recreate-db
docker-compose -f docker-compose-prod.yml run users python manage.py seed-db
