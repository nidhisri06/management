from django.urls import path, include
from .views import home
from .import views
from .views import dashboard

urlpatterns=[
    path('', views.home, name='home'),
    path('register/',views.visitor_registration,name='visitor_registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # urls.py
    path('accept/<int:id>/', views.accept_meet, name='accept_meet'),
    path('reject/<int:id>/', views.reject_meet, name='reject_meet'),
    path('reschedule/<int:id>/', views.reschedule_meet, name='reschedule_meet'),
    path('delete/<int:id>/', views.delete_meet, name='delete_meet'),


]