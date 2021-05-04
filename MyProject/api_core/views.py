from .mixins import GetSerializerClassMixin
from .serializers import UserSerializer,TeamSerializerGET,TeamSerializerPOST,ProofSerializerGET,ProofSerializerPOST,SessionSerializer,ChallengeSerializer
from .models import AppUser,Team,Proof,Session,Challenge
from rest_framework.authentication import SessionAuthentication,TokenAuthentication , BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
# Create your views here.

#User authentication related
from django.http import HttpResponseRedirect
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Creating modal view set, no need for functions as it's fully based on ModalAPI Views.
class UserViewSet(viewsets.ModelViewSet):
    #Defining model that we will retrieve data from
    queryset = AppUser.objects.all()
    #Defining serializer data that we want to display
    serializer_class = AppUser
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
