from django.urls import path
from .views import (
    face,
    hand,
    Camera)

urlpatterns = [
    path('', Camera.as_view(), name='camera'),
    path('video_face/', face, name='face'),
    path('video_hand/', hand, name='hand'),
]