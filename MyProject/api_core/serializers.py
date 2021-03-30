from rest_framework import serializers
from .models import User,Team,Proof,Session,Challenge

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','url','name', 'birthDate', 'email', 'teams']
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
    class Meta:
        model = Session
        fields = ['id', 'name','description','startDate','endDate']

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
