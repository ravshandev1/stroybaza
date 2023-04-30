from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryListAPIView.as_view()),
    path('subcategory/', views.SubCategoryListAPIView.as_view()),
    path('market-list/', views.MarketListAPIView.as_view()),
    path('product-list/', views.ProductListAPIView.as_view()),
    path('product-detail/', views.ProductDetailAPIView.as_view())
]
