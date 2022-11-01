#!/bin/sh
git pull
docker-compose -f docker-compose.prod.yml up -d --build web
docker-compose -f docker-compose.prod.yml restart nginx-proxy