from django.urls import path

from .views import create_drone, drone_list, get_drone, update_drone, delete_drone, news_get

urlpatterns = [
    path('drone-create/',create_drone, name='create-drone'),
    path('drone-list/',drone_list, name='drone_list'),
    path('drone-detail/<int:pk>/',get_drone, name='drone-detail'),
    path('drone-update/<int:pk>/',update_drone, name='drone-update'),
    path('drone-delete/<int:pk>/',delete_drone, name='drone-delete'),
    path('news/',news_get, name='news_get'),
]