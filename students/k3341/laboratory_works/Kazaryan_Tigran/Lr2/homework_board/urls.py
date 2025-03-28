from django.contrib import admin
from django.urls import path, include
from homework import views
from django.contrib.auth import views as auth_views
from homework.account_urls import home

urlpatterns = [
    path('admin/', admin.site.urls), #не трогаем
    path('auth/', include('django.contrib.auth.urls')),  #не трогаем
    path('homework/', include('homework.urls')), #не трогаем
    path('account/', include('homework.account_urls')), #не трогаем
    path('home/', home, name='home')
]
