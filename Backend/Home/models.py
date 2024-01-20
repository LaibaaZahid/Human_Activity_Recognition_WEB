from django.db import models

class User(models.Model):
    device_type = models.CharField(max_length=50)
    device_name = models.CharField(max_length=50)
# Create your models here.
