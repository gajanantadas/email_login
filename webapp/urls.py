from django.urls import path
from . import views
urlpatterns = [
    path('', views.view1, name='home'),
    path('r/', views.registration, name='reg'),
    path('l/', views.Userlogin, name='login'),
    path('logout/', views.logout, name='logout'),
    ]
