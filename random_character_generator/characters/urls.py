from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_random_character, name='generate_character'),
    path('save/', views.save_character, name='save_character'),
    path('archive/', views.character_archive, name='character_archive'),
]
