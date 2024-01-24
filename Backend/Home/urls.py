from django.contrib import admin
from django.urls import path, include
from Home import views
from .views import socket_connect

app_name = "Home"
urlpatterns = [
    # Socket pages
    path("", views.index, name= "index"),
    path("socket-connect/", views.socket_connect, name="socket_connect"),
    path("socket-disconnect/", views.disconnect, name="disconnect"),
    path("socket-binding/", views.socket_bind, name="bind"),
    path("active-users", views.get_active_users),
    path("all-users", views.get_all_users),
    path('api/device-users/', views.DeviceUserList.as_view(), name='device-user-list'),
    ]
