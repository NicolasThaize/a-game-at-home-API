from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, TeamViewSet, ProofViewSet, SessionViewSet, ChallengeViewSet, ArticleViewSet, \
    LogoutAndBlacklistRefreshTokenForUserView, TeamPointsViewSet, UserTeamAuthorizedViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithInfosView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('teams', TeamViewSet)
router.register('proofs', ProofViewSet)
router.register('sessions', SessionViewSet)
router.register('challenges', ChallengeViewSet)
router.register('articles', ArticleViewSet)
router.register('team_points', TeamPointsViewSet)
router.register('user_team_authorized', UserTeamAuthorizedViewSet)

urlpatterns = [
    # path('article/',article_list),
    # path('article/<int:pk>/',article_detail),
    # path('article/', ArticleAPIView.as_view()),
    # path('article/<int:pk>/',ArticleDetails.as_view()),
    path('', include(router.urls)),
    path('token/obtain/', ObtainTokenPairWithInfosView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist')
]
