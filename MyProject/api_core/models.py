from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    birthDate = models.DateField()
    teams = models.ManyToManyField('Team', blank=True)
    REQUIRED_FIELDS = ['birthDate', 'email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=50)
    totalPoints = models.IntegerField(default=0)
    users = models.ManyToManyField('CustomUser', related_name='team')
    sessions = models.ManyToManyField('Session', blank=True)

    def __str__(self):
        return self.name

class Proof(models.Model):
    photo = models.FileField(null=True)
    video = models.FileField(null=True)
    challenge = models.ManyToManyField('Challenge', blank=True)
    team = models.ManyToManyField(Team, blank=True)
    validated = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    def __str__(self):
        return self.id

class Session(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()
    teams = models.ManyToManyField('Team', related_name='session')

    def __str__(self):
        return self.name

class Challenge(models.Model):
    points = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    session = models.ForeignKey(Session,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    textContent = models.TextField(max_length=280)
    imageContent = models.ImageField()

    def __str__(self):
        return self.title
    

