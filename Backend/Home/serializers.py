from rest_framework import serializers
from .models import DeviceUser

class DeviceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceUser
        fields = '__all__'