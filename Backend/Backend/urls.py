
from django.contrib import admin
from django.urls import path, include
from . import views
from Home import urls
from Home.views import socket_connect
urlpatterns = [
    
    path('/', include(urls)),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls)  ,
    path('api/socket_connect', socket_connect, name='socket_connect')
    
    
    ]

