from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.LoginView, name = 'login'),
    path('home/contact/', views.Contact, name = 'contact'),
    path('videos/login/', views.LoginView, name = 'login'), 
    path('videos/signup/', views.SignupView, name = 'signup'), 
    path('logout/',views.LogoutView,name='logout'),
    path('signup/',views.SignupView,name='signup'),
    path('home/',views.Home, name= 'home'),
    path('forget-password/' , views.ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , views.ChangePassword , name="change_password"),
    path('',views.Index, name = 'index'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
