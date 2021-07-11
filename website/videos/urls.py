from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.VideosView, name ='videos'),
    path('upload/',views.UploadView,name='upload'),
    path('gallery/',views.Gallery,name='gallery'),
    path('gallery/<int:anomaly_id>',views.GalleryView,name='A_detail'),
    path('<int:video_id>', views.VideoDetailView, name='detail'),
    path('predict/<int:video_id>', views.saveFrame, name = 'frames'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)