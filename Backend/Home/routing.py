from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    
    # The line `re_path(r'ws/socket/$', consumers.MyConsumer.as_asgi())` is defining a URL pattern for
    # a WebSocket connection.
    re_path(r'ws/socket/$', consumers.MyConsumer.as_asgi()),
]
