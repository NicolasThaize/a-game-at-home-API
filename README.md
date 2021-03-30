#Start the project :

1:
    Install env component
    `pip install virtualenv`

2:
    create .env
    `virtualenv env`

3:
    activate it
    `.\env\Scripts\activate`

4:
    `pip install django`

5:
    `django-admin startproject MyAPI`

6:
    `cd .\src\` Should be default called MyAPI if that's the project name

7:
    Create Api core folders.
    `python manage.py startapp API`
8:
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








