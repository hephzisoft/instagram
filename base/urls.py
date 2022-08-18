from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('p/<uuid:post_id>/', views.feed, name='feed'),
    path('p/<uuid:post_id>/', views.like, name='like'),
]


