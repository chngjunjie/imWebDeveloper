from django.urls import path
from . import views

urlpatterns = [
    path('', views.lavaHome, name='lavaHome'),
    path('contact', views.contact, name='contact'),
]