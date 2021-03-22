from django.urls import path
from . import views

urlpatterns = [
    path('Disney', views.Disney, name='Disney'),
    path('Aurora', views.Aurora, name='Aurora'),
    path('Maldiv', views.Maldiv, name='Maldiv'),
    path('Prague', views.Prague, name='Prague'),
    path('Santor', views.Santor, name='Santor'),
    path('Scotla', views.Scotla, name='Scotla'),
    path('Venice', views.Venice, name='Venice'),
]
