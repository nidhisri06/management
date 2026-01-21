from django.urls import path, include
from .views import home
from .views import dashboard
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('register/', views.visitor_registration, name='visitor_registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
]