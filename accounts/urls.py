
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Register', views.Register,name='Register'),
    path('login',views.login,name='login'),
    path('logout', views.logout, name='logout'),
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('book',views.book,name='book'),
    path('pay',views.pay,name='pay'),
    path('sorry',views.sorry,name='sorry'),
    path('search',views.search,name='search'),
    path('comments',views.comments,name='comments'),
    ]