
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/detail/<str:slug>/', views.detail, name='detail'),
    path('post/create/', views.create_post, name="create"),
    path('post/update/<slug:slug>', views.update_post, name="update"),
    path('post/delete/<slug:slug>', views.delete_post, name="delete"),
]
