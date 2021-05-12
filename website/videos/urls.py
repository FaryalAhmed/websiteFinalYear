from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.VideosView, name = 'videos'),
    path('upload/',views.UploadView,name='upload'),
    path('<int:video_id>', views.VideoDetailView, name='detail'),
]