from django.contrib import admin
from .models import UserProfile
from tournament.models import Tournament


admin.site.register(UserProfile)
admin.site.register(Tournament)
