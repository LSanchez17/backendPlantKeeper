from django.apps import AppConfig
from django.contrib import admin
from .models import User

admin.site.register(User)

class PlantkeeperapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plantkeeperapi'
