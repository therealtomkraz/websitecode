#!/bin/bash -x

docker-compose down
sleep 3
docker volume prune -f
