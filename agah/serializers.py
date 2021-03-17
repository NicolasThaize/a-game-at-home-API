from rest_framework import serializers
from agah.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'birthDate', 'email', 'createdAt']