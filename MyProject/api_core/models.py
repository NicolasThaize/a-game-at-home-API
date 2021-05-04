from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.forms.fields import BooleanField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AppUser(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    birthDate = models.DateField()
    password = models.CharField(max_length=254)
    teams = models.ManyToManyField('Team',blank=True,null=True)
    REQUIRED_FIELDS = ['name', 'birthDate']
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50)
    totalPoints = models.IntegerField(default=0)
    users = models.ManyToManyField('AppUser')

    def __str__(self):
        return self.name

class Proof(models.Model):
    photo = models.FileField(null=True)
    video = models.FileField(null=True)
    challenge = models.ManyToManyField('Challenge',blank=True,null=True)
    team = models.ManyToManyField(Team,blank=True,null=True)
    validated = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)],default=0)

    def __str__(self):
        return self.id

class Session(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField()

    def __str__(self):
        return self.name

class Challenge(models.Model):
    points = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    session = models.ForeignKey(Session,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

