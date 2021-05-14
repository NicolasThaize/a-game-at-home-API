from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Team, UserTeamAuthorized, Proof, Session, Challenge, Article, TeamPoint

# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Team)
admin.site.register(UserTeamAuthorized)
admin.site.register(Proof)
admin.site.register(Session)
admin.site.register(Challenge)
admin.site.register(Article)
admin.site.register(TeamPoint)
