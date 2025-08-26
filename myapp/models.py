from django.db import models
import uuid

# Create your models here.

class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.locationName
    

class Item(models.Model):
    itemName = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName
    
class Product(models.Model):
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    label = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)