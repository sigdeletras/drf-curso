# geo-api-drf

geo-api-drf

17 Linting and test

docker-compose run --rm app sh -c "flake8"

docker-compose run --rm app sh -c "python manage.py test"

19 Build django project

docker-compose run --rm app sh -c "django-admin startproject ."

docker-compose run --rm app sh -c "django-admin startproject app ."
