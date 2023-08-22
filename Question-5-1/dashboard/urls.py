from django.urls import path
from . import views


#Create urls here

urlpatterns = [
    path('', views.landing, name='landing'),
]
