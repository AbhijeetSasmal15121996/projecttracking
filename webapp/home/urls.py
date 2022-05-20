from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('hodsigin', views.hodsignin, name='hodsignin'),
    path('hodsignup', views.hodsignup, name='hodsignup'),
    path('cordsignin', views.corsignin, name='cordsignin'),
    path('cordsignup', views.corsignup, name='cordsignup'),
    path('cord', views.cordination, name='cord'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('cord_details', views.cord_details, name='cord_details'),
    path('coorreview', views.coorreview, name='corview'),
    path('logout', views.logout, name='logout'),
    path('hod', views.hod, name='hod'),
    path('guide', views.guide, name='guide'),
    path('guides', views.guides, name='guides'),
    path('teamsignup1', views.teamsignup1, name='teamsignup1'),
    
]