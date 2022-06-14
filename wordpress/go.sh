#!/bin/bash -x


docker-compose up -d
sleep 30
docker-compose run --rm wp-cli install-wp
