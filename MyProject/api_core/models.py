from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    birth_date = models.DateField()
    teams = models.ManyToManyField('Team', blank=True)
    REQUIRED_FIELDS = ['birth_date', 'email', 'first_name', 'last_name']

    def __str__(self):
        return self.username


class Team(models.Model):
    name = models.CharField(max_length=50)
    total_points = models.IntegerField(default=0)
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
    start_date = models.DateField()
    end_date = models.DateField()
    teams = models.ManyToManyField('Team', related_name='session')

    def __str__(self):
        return self.name


class Challenge(models.Model):
    points = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    session = models.ForeignKey(Session, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    text_content = models.TextField(max_length=280)
    image_url = models.charField(max_length=255)

    def __str__(self):
        return self.title
