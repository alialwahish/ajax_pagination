
from __future__ import unicode_literals
from django.db import models
import datetime

class Users(models.Model):
    lead_id = models.IntegerField()
    first_name= models.CharField(max_length = 255)
    last_name= models.CharField(max_length = 255)
    email= models.CharField(max_length = 255)
    registered_datetime = models.DateField()