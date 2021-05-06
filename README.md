#Start the project :

1:
    `pip install django`
    `pip install djangorestframework`
    `pip install djangorestframework-simplejwt`
    `pip install django-cors-headers`
    

2:
    `django-admin startproject MyAPI`

3:
    `cd .\src\` Should be default called MyAPI if that's the project name

4:
    Create Api core folders.
    `python manage.py startapp API`
5:
    Install the REST framework
    `pip install djangorestframework`

#Basic commands

#Migrations

Make new migrations based on models, use before "migrate"
`python manage.py makemigrations`

Apply migrations to database
`python manage.py migrate`
Should have everything say ...OK

#Development server

run API server
`python manage.py runserver`
Should have running server URL as result if successful.








