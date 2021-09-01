from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic_url = models.URLField()
    location = models.IntegerField()
    password = models.CharField(max_length=500)
    fully_set_up = models.BooleanField()

class Weather(models.Model):
    location = models.IntegerField()
    date = models.DateField()
    forecast = models.TextField()
    user_id = models.ForeignKey()

class Plant(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    plant_name = models.CharField(max_length=30)
    plant_birthday = models.DateField()
    last_watered = models.DateField()
    last_trimmed = models.DateField()
    last_repotted = models.DateField()
    indoor = models.BooleanField()
    user_id = models.ForeignKey()