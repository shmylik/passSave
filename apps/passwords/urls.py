from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_passwords, name='get_passwords'),
]