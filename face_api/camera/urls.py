from django.urls import path
from .views import (
    livefe,
    Camera)

urlpatterns = [
    path('', Camera.as_view(), name='camera'),
    path('video_feed/', livefe, name='livefe'),
]