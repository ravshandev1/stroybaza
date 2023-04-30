from rest_framework import generics, permissions, response
from .serializers import CardItemSerializer, OrderSerializer
from .models import Order, CardItem


class CardItemAPI(generics.CreateAPIView):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer


class OrderAPI(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        qs = self.queryset.filter(user_id=self.request.user.id).all()
        serializer = self.get_serializer(qs, many=True)
        return response.Response(serializer.data)
