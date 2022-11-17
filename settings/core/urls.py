from django.contrib import admin
from django.urls import path
from .views import aPage
   
urlpatterns = [
    path('', aPage),
]