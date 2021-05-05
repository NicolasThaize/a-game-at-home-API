from rest_framework import serializers
from .models import CustomUser,Team,Proof,Session,Challenge

# Auth related:

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Adding all needed informations to token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom fields
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email

        return token



###################################################################################
class UserSerializer(serializers.ModelSerializer):
    birthDate = serializers.DateField(input_formats=['%d-%m-%Y',])
    class Meta:
        model = CustomUser
        fields = ['id','url','username', 'first_name', 'last_name', 'birthDate', 'email', 'teams']
###################################################################################
class TeamSerializerGET(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    class Meta:
        model = Team
        fields = ['id', 'url', 'name', 'totalPoints', 'users']

class TeamSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'url', 'name', 'totalPoints', 'users']
###################################################################################

class SessionSerializer(serializers.ModelSerializer):
    teams = TeamSerializerGET(many=True)
    class Meta:
        model = Session
        fields = ['id', 'name','description','startDate','endDate', 'teams']

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id','name','points','description','session']

###################################################################################

class ProofSerializerGET(serializers.ModelSerializer):
    challenge = ChallengeSerializer(many=True)
    team = TeamSerializerGET(many=True)
    class Meta:
        model = Proof
        fields = ['id','photo','video','challenge','team','validated']

class ProofSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Proof
        fields = ['id','photo','video','challenge','team','validated']
