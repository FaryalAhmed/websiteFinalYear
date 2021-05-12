from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', views.LoginView, name = 'login'),
    path('videos/login/', views.LoginView, name = 'login'), 
    path('videos/signup/', views.SignupView, name = 'signup'), 
    path('logout/',views.LogoutView,name='logout'),
    path('signup/',views.SignupView,name='signup'),
    path('home/',views.Home, name= 'home'),
    path('',views.Index, name = 'index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
