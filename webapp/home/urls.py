from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('hod', views.hodsignin, name='hodsignin'),
    path('hodsignup', views.hodsignup, name='hodsignup'),
]