from .mixins import GetSerializerClassMixin
from .models import User,Team,Proof,Session,Challenge
from .serializers import UserSerializer,TeamSerializerGET,TeamSerializerPOST,ProofSerializerGET,ProofSerializerPOST,SessionSerializer,ChallengeSerializer
from .models import User,Team,Proof,Session,Challenge
from rest_framework.authentication import SessionAuthentication,TokenAuthentication , BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.

#Creating modal view set, no need for functions as it's fully based on ModalAPI Views.
class UserViewSet(viewsets.ModelViewSet):
    #Defining model that we will retrieve data from
    queryset = User.objects.all()
    #Defining serializer data that we want to display
    serializer_class = UserSerializer
    #Defining authentication methods for this view.
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #Defining simple method that lets user access view if authenticated by any mean
    permission_classes = [IsAuthenticated]

class TeamViewSet(GetSerializerClassMixin,viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializerPOST

    #Defining dynamic serializer choice depending on which request type user does
    serializer_action_classes = {
        'list': TeamSerializerGET,
        'retrieve' : TeamSerializerGET,
    }
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ProofViewSet(GetSerializerClassMixin,viewsets.ModelViewSet):
    queryset = Proof.objects.all()
    serializer_class = ProofSerializerPOST
    serializer_action_classes = {
        'list': ProofSerializerGET,
        'retrieve' : ProofSerializerGET,
    }
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
