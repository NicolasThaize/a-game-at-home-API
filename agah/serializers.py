from rest_framework import serializers
from agah.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(primary_key=True)
    firstName = serializers.CharField(max_length=50)
    lastName = serializers.CharField(max_length=50)
    birthDate = serializers.DateTimeField()
    email = serializers.CharField(max_length=60)
    password = serializers.CharField()
    createdAt = serializers.DateTimeField(auto_now_add=True)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.birthDate = validated_data.get('birthDate', instance.lastName)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
