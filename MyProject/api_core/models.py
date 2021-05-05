from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.forms.fields import BooleanField
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    birthDate = models.DateField()
    teams = models.ManyToManyField('Team',blank=True)
    REQUIRED_FIELDS = ['birthDate', 'email', 'first_name', 'last_name']
    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=50)
    totalPoints = models.IntegerField(default=0)
    users = models.ManyToManyField('CustomUser')

    def __str__(self):
        return self.name

class Proof(models.Model):
    photo = models.FileField(null=True)
    video = models.FileField(null=True)
    challenge = models.ManyToManyField('Challenge',blank=True)
    team = models.ManyToManyField(Team,blank=True)
    validated = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)],default=0)

    def __str__(self):
        return self.id

class Session(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField()
    teams = models.ManyToManyField('Team',blank=True)

    def __str__(self):
        return self.name

class Challenge(models.Model):
    points = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    session = models.ForeignKey(Session,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

