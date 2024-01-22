from django.contrib import admin
from django.urls import path, include
from Home import views
from .views import socket_connect

app_name = "Home"
urlpatterns = [
    # Socket pages
    path("", views.index, name= "index"),
    path("api/socket_connect", views.socket_connect, name="socket_connect"),
    path("disconnect", views.disconnect, name="disconnect"),
    path("socket-binding", views.socket_bind, name="bind")
]
