
from django.contrib import admin
from django.urls import path, include
from .views import *

from Home import urls

urlpatterns = [
    
    # path('/', include(urls)), """
    path('', index),
    path('admin/', admin.site.urls)  ,
    
    ]

