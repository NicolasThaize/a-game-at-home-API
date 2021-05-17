from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    birth_date = models.DateField()
    teams = models.ManyToManyField('Team', blank=True)
    authorized_teams = models.ManyToManyField('UserTeamAuthorized', blank=True)

    REQUIRED_FIELDS = ['birth_date', 'email', 'first_name', 'last_name']

    def __str__(self):
        return self.username


class Proof(models.Model):
    photo = models.FileField(null=True, blank=True, upload_to='proofsPhotos/', default='proofsPhotos/None/No-img.jpg')
    video = models.FileField(null=True, blank=True, upload_to='proofsVideos/', default='proofsVideos/None/No-video.jpg')
    challenge = models.ManyToManyField('Challenge', blank=True)
    sessions = models.ManyToManyField('Session', blank=True)
    teams = models.ManyToManyField('Team')
    validated = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], default=3)

    def __str__(self):
        return str(self.id)


class Team(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField('CustomUser', related_name='team', blank=True)
    sessions = models.ManyToManyField('Session', blank=True)
    session_points = models.ManyToManyField('TeamPoint', blank=True)
    authorized_users = models.ManyToManyField('UserTeamAuthorized', blank=True)
    session_proofs = models.ManyToManyField('Proof', related_name="team", blank=True)

    def __str__(self):
        return self.name


class UserTeamAuthorized(models.Model):
    teams = models.ManyToManyField('Team', related_name='authorized_user')
    users = models.ManyToManyField('CustomUser', related_name='authorized_team')

    def __str__(self):
        return self.id


class Challenge(models.Model):
    points = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    teams = models.ManyToManyField('Team', related_name='session', blank=True)
    team_points = models.ManyToManyField('TeamPoint', blank=True)
    challenges = models.ManyToManyField(Challenge, blank=True)
    team_proofs = models.ManyToManyField(Proof, blank=True, related_name='session')

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    image_url = models.CharField(max_length=254, default='')
    text_content = models.TextField(max_length=280)

    def __str__(self):
        return self.title


class TeamPoint(models.Model):
    points = models.IntegerField(default=0)
    teams = models.ManyToManyField('Team', related_name='session_point')
    sessions = models.ManyToManyField('Session', related_name='team_point')

    def __str__(self):
        return self.points
