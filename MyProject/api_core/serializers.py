from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser, Team, UserTeamAuthorized, Proof, Session, Challenge, Article, TeamPoint


# Auth related:

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
        token['birth_date'] = user.birth_date.strftime("%d-%m-%Y")
        token['admin'] = user.is_superuser

        return token


###################################################################################
class UserSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(input_formats=['%d-%m-%Y', ])

    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'birth_date', 'email', 'team', 'password',
                  'authorized_team']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birth_date=validated_data['birth_date'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        print(validated_data)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
            instance.save()
            return instance


###################################################################################
class TeamSerializerGET(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'url', 'name', 'session', 'users', 'session_point', 'authorized_user']


class TeamSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'url', 'name', 'session', 'users', 'session_point', 'authorized_user']


###################################################################################

class UserTeamAuthorizedSerializer(serializers.ModelSerializer):
    teams = TeamSerializerGET
    users = UserSerializer

    class Meta:
        model = UserTeamAuthorized
        fields = ['id', 'teams', 'users']


###################################################################################

class SessionSerializerGET(serializers.ModelSerializer):
    start_date = serializers.DateField(input_formats=['%d-%m-%Y', ])
    end_date = serializers.DateField(input_formats=['%d-%m-%Y', ])
    teams = TeamSerializerGET(many=True)

    class Meta:
        model = Session
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'teams', 'team_point']


class SessionSerializerPOST(serializers.ModelSerializer):
    start_date = serializers.DateField(input_formats=['%d-%m-%Y', ])
    end_date = serializers.DateField(input_formats=['%d-%m-%Y', ])

    class Meta:
        model = Session
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'teams', 'team_point']


###################################################################################
class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'name', 'points', 'description', 'session']


###################################################################################

class ProofSerializerGET(serializers.ModelSerializer):
    challenge = ChallengeSerializer(many=True)
    team = TeamSerializerGET(many=True)

    class Meta:
        model = Proof
        fields = ['id', 'photo', 'video', 'challenge', 'team', 'validated']


class ProofSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Proof
        fields = ['id', 'photo', 'video', 'challenge', 'team', 'validated']


###################################################################################
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'text_content', 'image_url']


###################################################################################

class TeamPointSerializer(serializers.ModelSerializer):
    teams = TeamSerializerGET
    sessions = SessionSerializerGET

    class Meta:
        model = TeamPoint
        fields = ['id', 'teams', 'sessions', 'points']
