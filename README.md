
## GDAL

Library for geo calculation.

1. Install gdal for mac os `brew install gdal`
1. Install gdal for unix `[sudo] apt-get install gdal-bin`

## Docker

1. Run into docker: `docker-compose up` or rebuild `docker-compose up --build`
1. Migrage (after run): `docker-compose run api python manage.py migrate`

## Lint

Run pylint for development `pylint --load-plugins pylint_django service`

## Test

Run test for development in docker `docker-compose run api python manage.py test`
