from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    """ User model """
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
    """ Weather model """
    location = models.IntegerField()
    date = models.DateField()
    forecast = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Plant(models.Model):
    """ Plant Model """
    id = models.CharField(primary_key=True, max_length=30)
    plant_name = models.CharField(max_length=30)
    plant_birthday = models.DateField()
    last_watered = models.DateField()
    last_trimmed = models.DateField()
    last_repotted = models.DateField()
    indoor = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=CASCADE)