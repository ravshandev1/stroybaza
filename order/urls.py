from django.urls import path
from .views import OrderAPI, CardItemAPI

urlpatterns = [
    path('', OrderAPI.as_view()),
    path('card-item/', CardItemAPI.as_view()),
]
