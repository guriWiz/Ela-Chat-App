from django.urls import path
from . import views 
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.Home.as_view(), name="Home"),
    path("accounts/register/", views.register, name="Register"),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='Dashboard'),
    path('room/', TemplateView.as_view(template_name='room.html'), name='Room'),
    path('search_user/', views.SearchUser.as_view(), name='Search_User'),
    path('update_profile/', views.UpdateProfile, name='Update_Profile'),
    path('room/<str:room_name>/', views.room, name='RoomLobby'),
]