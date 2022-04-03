from django.urls import include, path
from gallery.views import (CreatePhotoView, PhotoListView, PhotoDeleteView,
                            PhotoUpdateView, GalleryView, CreateVideoView,
                            VideoListView, VideoDeleteView)

app_name ='gallery'
urlpatterns = [
    path('createphoto/', CreatePhotoView, name='createphoto'),
    path('createvideo/', CreateVideoView, name='createvideo'),
    path('photo-list/', PhotoListView, name='photolist'),
    path('video-list/', VideoListView, name='videolist'),
    path('photo-delete/<int:pk>/', PhotoDeleteView, name='photodelete'),
    path('video-delete/<int:pk>/', VideoDeleteView, name='videodelete'),
    path('photo-update/<int:pk>/', PhotoUpdateView, name='photoupdate'),
    path('gallery/', GalleryView, name='gallery'),

]
