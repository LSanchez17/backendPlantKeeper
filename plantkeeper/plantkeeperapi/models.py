from django.db import models

# Create your models here.
# migrate if you make changes here 
class User(models.Model):
    """ User Model """
    id = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic_url = models.URLField()
    location = models.IntegerField()
    password = models.CharField(max_length=30)
    fully_set_up = models.BooleanField()
    private = models.BooleanField()
    # make a one to many table friends
    # make a one to many table friend_requests = ''



    def __str__(self):
        return self.name


class Plants(models.Model):
    """ Plants model """
    id = models.CharField(max_length=10, primary_key=True)
    plant_name = models.CharField(max_length=50)
    plant_birthday = models.DateTimeField()
    last_water = models.DateTimeField()
    last_trim = models.DateTimeField()
    last_repot = models.DateTimeField()
    indoor = models.BooleanField
    notes = models.TextField()
    plant_pic = models.TextField()


class Weather(models.Model):
    """ Weather model """

    location = models.IntegerField()
    date = models.DateTimeField()
    forecast = models.TextField()
    