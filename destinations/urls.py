
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('offers',views.offers, name='offers'),
    path('desert',views.desert,name='desert'),
    path('fly',views.fly,name='fly'),
    path('water',views.water,name='water'),
    path('destinations',views.destinations,name='destinations'),

]
