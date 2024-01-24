
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class DeviceUser(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    device_type = models.CharField(max_length=20, choices=[('smartphone', 'Smartphone'), ('smartwatch', 'Smartwatch'), ('glasses', 'Glasses')])
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    last_connected = models.DateTimeField()


