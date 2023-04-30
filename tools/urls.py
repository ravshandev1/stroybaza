from django.urls import path
from . import views

urlpatterns = [
    path('slider/', views.SliderListAPIView.as_view()),
    path('location-list/', views.LocationListAPIView.as_view()),
    path('location-create/', views.LocationCreateAPIView.as_view()),
    path('location-rud/<int:pk>/', views.LocationRUDAPIView.as_view())
]
