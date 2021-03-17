from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *


# Create your views here.


# class ArticleViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
#    serializer_class = ArticleSerializer
#    queryset = Article.objects.all()

class UserViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
