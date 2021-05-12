from .mixins import GetSerializerClassMixin
from .serializers import UserSerializer, TeamSerializerGET, TeamSerializerPOST, ProofSerializerGET, \
    ProofSerializerPOST, SessionSerializerGET, SessionSerializerPOST, ChallengeSerializer, ArticleSerializer
from .models import CustomUser, Team, Proof, Session, Challenge, Article
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status

from .permissions import IsPostOrIsAuthenticated, IsGetOrIsAuthenticated

# Create your views here.
# Auth related:
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response


class ObtainTokenPairWithInfosView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Creating modal view set, no need for functions as it's fully based on ModalAPI Views.
class UserViewSet(viewsets.ModelViewSet):
    # Defining model that we will retrieve data from
    queryset = CustomUser.objects.all()
    # Defining serializer data that we want to display
    serializer_class = UserSerializer
    # Defining authentication methods for this view.
    # Defining simple method that lets user access view if authenticated by any mean
    permission_classes = [IsPostOrIsAuthenticated]


class TeamViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializerPOST

    # Defining dynamic serializer choice depending on which request type user does
    serializer_action_classes = {
        'list': TeamSerializerGET,
        'retrieve': TeamSerializerGET,
    }
    permission_classes = [IsAuthenticated]


class ProofViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = Proof.objects.all()
    serializer_class = ProofSerializerPOST
    serializer_action_classes = {
        'list': ProofSerializerGET,
        'retrieve': ProofSerializerGET,
    }
    permission_classes = [IsAuthenticated]


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializerPOST
    serializer_action_classes = {
        'list': SessionSerializerGET,
        'retrieve': SessionSerializerGET,
    }
    permission_classes = [IsGetOrIsAuthenticated]


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsGetOrIsAuthenticated]
