from django.urls import path
from . import views

#my urls here

urlpatterns = [
    path('', views.home, name='home'),

]