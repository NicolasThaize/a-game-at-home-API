from django.contrib import admin
from .models import User,Team,Proof,Session,Challenge

# Register your models here.

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Proof)
admin.site.register(Session)
admin.site.register(Challenge)
