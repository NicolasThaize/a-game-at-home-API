from django.contrib import admin
from .models import AppUser,Team,Proof,Session,Challenge

class CustomUserAdmin(admin.ModelAdmin):
    model = AppUser

# Register your models here.

admin.site.register(AppUser, CustomUserAdmin)
admin.site.register(Team)
admin.site.register(Proof)
admin.site.register(Session)
admin.site.register(Challenge)
