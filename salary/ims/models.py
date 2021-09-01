from os import name
from django.db import models
import datetime
from django.db.models.fields import related

# Create your models here.


class Unit(models.Model):
    name = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=datetime.datetime.now())
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    unit = models.ForeignKey(Unit, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=datetime.datetime.now())
    def __str__(self):
        return self.name

class ItemType(models.Model):
    name = models.CharField(max_length=100, null=True)
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    salePrice = models.IntegerField(null=True)
    purchasePrice = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=datetime.datetime.now())
    def __str__(self):
        return self.name

class Invoice(models.Model):
    customer = models.CharField(max_length=100, null=True)
    #product = models.ManyToManyField(ItemType)
    products = models.ForeignKey(ItemType, on_delete=models.CASCADE, null=True)
    notes = models.CharField(max_length=245, null=True)