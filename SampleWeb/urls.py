"""SampleWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Required modules
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#These are the urls which will direct the user to the specified page
urlpatterns = [
    #The admin url can be accessed by the creator only.. noone else can aceess it
    #Only creator can add items to the website dynamically
    path('admin/', admin.site.urls),

    #This is the main page of website
    path('', include('travello.urls')),

    #This page manages accounts
    path('accounts/',include('accounts.urls')),

    #This page informs the users about the places and all
    path('destinations/',include('destinations.urls')),

    #This page is for learning about the hotels and other things about a specific place
    path('hotels/',include('hotels.urls'))

]

#This command helps to accomodate all the urls in a single webpage
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)