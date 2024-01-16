from django.urls import path

from . import consumers
from Home import views
websocket_urlpatterns = [
    path('', consumers.MyConsumer.as_asgi()),
    path('', views.index, name='index'),
    path('socket-connect', views.socket_connect, name="socket")
]
