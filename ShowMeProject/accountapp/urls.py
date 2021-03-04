from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', views.register_fun, name='register'),
    path('login/', views.login_fun, name='login'),
    path('logout/', views.logout_fun, name='logout'),
    path('profile/', views.profile_fun, name='profile'),
    path('activate/', views.activate_fun, name='activate'),
]
