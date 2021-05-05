from .mixins import GetSerializerClassMixin
from .serializers import UserSerializer,TeamSerializerGET,TeamSerializerPOST,ProofSerializerGET,ProofSerializerPOST,SessionSerializer,ChallengeSerializer
from .models import CustomUser,Team,Proof,Session,Challenge
from rest_framework.authentication import SessionAuthentication,TokenAuthentication , BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .permissions import IsPostOrIsAuthenticated

# Create your views here.
# Auth related:
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from .serializers import MyTokenObtainPairSerializer
class ObtainTokenPairWithInfosView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

#Creating modal view set, no need for functions as it's fully based on ModalAPI Views.
class UserViewSet(viewsets.ModelViewSet):
    #Defining model that we will retrieve data from
    queryset = CustomUser.objects.all()
    #Defining serializer data that we want to display
    serializer_class = UserSerializer
    #Defining authentication methods for this view.
    #Defining simple method that lets user access view if authenticated by any mean
    permission_classes = [IsPostOrIsAuthenticated]

class TeamViewSet(GetSerializerClassMixin,viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializerPOST

    #Defining dynamic serializer choice depending on which request type user does
    serializer_action_classes = {
        'list': TeamSerializerGET,
        'retrieve' : TeamSerializerGET,
    }
    permission_classes = [IsAuthenticated]


class ProofViewSet(GetSerializerClassMixin,viewsets.ModelViewSet):
    queryset = Proof.objects.all()
    serializer_class = ProofSerializerPOST
    serializer_action_classes = {
        'list': ProofSerializerGET,
        'retrieve' : ProofSerializerGET,
    }
    permission_classes = [IsAuthenticated]

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated]
