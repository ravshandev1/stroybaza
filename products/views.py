from .models import Category, SubCategory, Market, Product
from .serializers import CategorySerializer, SubCategorySerializer, MarketSerializer, ProductSerializer
from rest_framework import generics


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListAPIView(generics.ListAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        queryset = SubCategory.objects.all()
        pk = self.request.GET.get('category')
        if pk:
            queryset = SubCategory.objects.filter(category_id=pk)
        return queryset


class MarketListAPIView(generics.ListAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        market = self.request.GET.get('market')
        category = self.request.GET.get('category')
        max_price = self.request.GET.get('max_price')
        min_price = self.request.GET.get('min_price')
        color = self.request.GET.get('color')
        if market:
            queryset = queryset.filter(market_id=market)
        if category:
            queryset = queryset.filter(category_id=category)
        if max_price:
            queryset = queryset.filter(price__lt=max_price)
        if min_price:
            queryset = queryset.filter(price__lt=min_price)
        if color:
            queryset = queryset.filter(color__color=color)
        return queryset


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
