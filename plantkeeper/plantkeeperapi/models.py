from django.db import models

# Create your models here.
# migrate if you make changes here 
class User(models.Model):
    """ User Model """
    id = ''
    username = ''
    email = ''
    first_name = ''
    last_name = ''
    profile_pic_url = ''
    location = ''
    password = ''
    fully_set_up = ''
    private = ''
    friend_set = ''
    friend_requests = ''



    def __str__(self):
        return self.name


class Plants(models.Model):
    """ Plants model """
    id = ''
    plant_name = ''
    plant_birthday = ''
    last_water = ''
    last_trim = ''
    last_repot = ''
    indoor = ''
    notes = ''
    plant_pic = ''


class Weather(models.Model):
    """ Weather model """

    location = ''
    date = ''
    forecast = ''
    