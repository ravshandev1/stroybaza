from django.urls import path
from .views import MyAccountRUDAPIView, LogoutView, VerifyPhoneAPIView, LoginView, UserCardAPI, UserCardRUDAPI

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('verify-phone/', VerifyPhoneAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('card/', UserCardAPI.as_view()),
    path('card/<int:pk>/', UserCardRUDAPI.as_view()),
    path('logout/', LogoutView.as_view()),
    path('account-rud/<int:pk>/', MyAccountRUDAPIView.as_view())
]
