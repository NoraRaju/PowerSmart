from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('appliance/', views.appliances, name="app"),
    path('room/', views.room, name="room"),
    path('cost/', views.cost, name="cost"),
    path('about/', views.about, name="about"),
    path('contact-us/', views.contact, name="contact"),
]