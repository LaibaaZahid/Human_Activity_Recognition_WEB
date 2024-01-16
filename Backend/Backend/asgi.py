"""
ASGI config for Backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import Home.routing
from Home.consumers import *
from Home import views
from django.urls import path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')

#ws_patterns = [ path('ws/test/', MyConsumer), path('', views.index, name='index')]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
            Home.routing.websocket_urlpatterns),
        #ws_patterns),
})