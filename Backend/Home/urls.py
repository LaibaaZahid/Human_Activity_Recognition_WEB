from django.contrib import admin
from django.urls import path, include
from Home import views
urlpatterns = [
    # Socket pages
    path("index", views.index, name= "index"),
    path('socket-connect', views.socket_connect, name="socket")
]
