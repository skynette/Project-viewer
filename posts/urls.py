
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/detail/<str:slug>/', views.detail, name='detail'),
]
