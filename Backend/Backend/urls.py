
from django.contrib import admin
from django.urls import path, include
from . import views

from Home import urls

urlpatterns = [
    
    # path('/', include(urls)), """
    path('', views.index, name='index'),
    path('admin/', admin.site.urls)  ,
    
    ]

