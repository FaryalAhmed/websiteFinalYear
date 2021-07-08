from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.LoginView, name = 'login'),
    path('videos/login/', views.LoginView, name = 'login'), 
    path('videos/signup/', views.SignupView, name = 'signup'), 
    path('logout/',views.LogoutView,name='logout'),
    path('signup/',views.SignupView,name='signup'),
    path('home/',views.Home, name= 'home'),
    path('reset-password/',auth_views.PasswordResetView.as_view(),name='reset'),
    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),
    path('',views.Index, name = 'index'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
