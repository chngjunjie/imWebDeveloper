from django.urls import path
from . import views

urlpatterns = [
    path('lava', views.lavaHome, name='lava'),
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
]