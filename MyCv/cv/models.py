from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class CV (models.Model):

    class User(models.Model):
        first_name = models.CharField(max_length=200)
        last_name = models.CharField(max_length=200)
        address = models.CharField(max_length=500)
        telephone = models.BigIntegerField()
        email = models.EmailField

    class JobTitle(models.Model):
        jobtitle_text = models.CharField(max_length=200)

