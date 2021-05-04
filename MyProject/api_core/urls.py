from django.contrib import admin
from django.urls import path,include
from .views import UserViewSet,TeamViewSet,ProofViewSet,SessionViewSet,ChallengeViewSet, current_user, UserList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('teams', TeamViewSet)
router.register('proofs', ProofViewSet)
router.register('sessions', SessionViewSet)
router.register('challenge', ChallengeViewSet)

urlpatterns = [
    #path('article/',article_list),
    #path('article/<int:pk>/',article_detail),
    #path('article/', ArticleAPIView.as_view()),
    #path('article/<int:pk>/',ArticleDetails.as_view()),
    path('',include(router.urls)),
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]
