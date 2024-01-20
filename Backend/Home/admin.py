from django.contrib import admin
from Home.models import User

class userAdmin(admin.ModelAdmin):
    list_display=('device_type', 'device_name')

admin.site.register(User, userAdmin )    
# Register your models here.
