from django.urls import path
from . import views

urlpatterns = [
    path('divide/', views.operation),
    #path('user_mgmt/', views.index)
    path('page/', views.login),
    #path('homepage/', views.home)
    path('insertdb/', views.insertdata),
    path('disp/', views.displayTable),
    path('editPage/<int:id>', views.editTable)
]