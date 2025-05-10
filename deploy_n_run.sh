#!/bin/bash
echo "Starting Docker containers..."
docker compose down
docker compose -f docker-compose.yml -f docker-compose.prod.yml build
docker compose run web python manage.py migrate
docker compose run web python manage.py collectstatic --noinput
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

echo "Application is running at http://localhost:80"