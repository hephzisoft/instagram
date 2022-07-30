from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('p/<str:pk>/', views.feed, name='feed'),
    path('p/<str:pk>/', views.like, name='like')
]


