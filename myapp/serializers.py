from rest_framework import serializers
from .models import Item, Location,Product

class ItemSerializer(serializers.ModelSerializer):
     class Meta:
        model = Item
        fields = ('__all__')

class LocationSerializer(serializers.ModelSerializer):
     class Meta:
        model = Location
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')