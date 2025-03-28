from django.urls import path
from .views import register, homework_list, home, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('list/', homework_list, name='homework_list'),
    path('profile/', profile, name='profile'),
]

