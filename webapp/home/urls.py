from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('hod', views.hodsignin, name='hodsignin'),
    path('hodsignup', views.hodsignup, name='hodsignup'),
    path('cordsignin', views.corsignin, name='cordsignin'),
    path('cordsignup', views.corsignup, name='cordsignup'),
    path('coor', views.cordination, name='cord'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    
]