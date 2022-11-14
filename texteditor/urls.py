from django.contrib import admin
from django.urls import path
from texteditor import views
urlpatterns = [
    path('', views.homeView, name='texteditor_home')
]