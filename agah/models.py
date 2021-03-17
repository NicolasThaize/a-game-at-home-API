from django.db import models


# Create your models here.

class User(models.Model):
    class Meta:
        db_table = 'user'

    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    birthDate = models.DateField()
    email = models.CharField(max_length=60)
    password = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
