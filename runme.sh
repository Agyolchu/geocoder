#!/bin/bash

docker-compose build
docker-compose up -d redis rabbit
shell_scripts/run_celery.sh
