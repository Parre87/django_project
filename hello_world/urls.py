from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.list_destinations, name='list_destinations'),
    path('book/', views.book_destination, name='book_destination'),
    path('dashboard/', views.dashboard, name='dashboard'),]
# This file defines the URL patterns for the hello_world app, mapping URLs to views.