from .mixins import GetSerializerClassMixin
from .models import User,Team,Proof,Session,Challenge
from .serializers import UserSerializer,TeamSerializerGET,TeamSerializerPOST,ProofSerializerGET,ProofSerializerPOST,SessionSerializer,ChallengeSerializer
from .models import User,Team,Proof,Session,Challenge
from rest_framework.authentication import SessionAuthentication,TokenAuthentication , BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TeamViewSet(GetSerializerClassMixin,viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializerPOST
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
