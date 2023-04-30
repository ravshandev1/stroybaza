from rest_framework.response import Response
from .serializers import LocationSerializer, SliderSerializer
from .models import Location, Slider
from rest_framework import generics, status, authentication


class SliderListAPIView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class LocationListAPIView(generics.ListAPIView):
    serializer_class = LocationSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        queryset = Location.objects.filter(user=user)
        return queryset


class LocationCreateAPIView(generics.CreateAPIView):
    serializer_class = LocationSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        data = request.data
        data['user'] = user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LocationRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Location.objects.all()
