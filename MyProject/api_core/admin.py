from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Team,Proof,Session,Challenge

# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Team)
admin.site.register(Proof)
admin.site.register(Session)
admin.site.register(Challenge)
