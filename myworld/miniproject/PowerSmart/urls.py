from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('appliance/', views.appliances, name="app"),
    path('room/', views.room, name="room")
]