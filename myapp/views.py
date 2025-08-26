from rest_framework import generics
# from django.shortcuts import render, get_object_or_404, redirect

from .models import Item, Location, Product
from .serializers import ItemSerializer, LocationSerializer, ProductSerializer

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')

        if location is not None:
            queryset = queryset.filter(ItemLocation=Location)
            
            return queryset
        
class ItemDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()