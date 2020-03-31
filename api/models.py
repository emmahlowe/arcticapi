from django.db import models
from api.fields import JSONField
from rest_framework import routers, serializers, viewsets

# Create your models here.
class Category(models.Model):
    title = models.TextField()

# Serializers define the API representation
# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['title']

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.TextField()
    description = models.TextField()
    filename = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Sale(models.Model):
    name = models.TextField()
    address1 = models.TextField()
    address2 = models.TextField(null=True, blank=True)
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    items = JSONField(default=dict)
    payment_intent = JSONField(default=dict)
