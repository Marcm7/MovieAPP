from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('add/', views.video_create, name='video_create'),
    path('<int:pk>/edit/', views.video_update, name='video_update'),
    path('<int:pk>/delete/', views.video_delete, name='video_delete'),
]
