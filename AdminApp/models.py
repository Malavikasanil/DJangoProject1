from django.db import models

# Create your models here.
class Category(models.Model):
    CategoryName = models.CharField(max_length=100, null=True, blank=True)
    CategoryImage = models.ImageField(upload_to="Categories", null=True, blank=True)
    CategoryDesc = models.TextField(max_length=600, null=True, blank=True)

class Product(models.Model):
    ProductCat = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    ProductQuantity = models.IntegerField(null=True, blank=True)
    ProductPrice = models.IntegerField(null=True, blank=True)
    ProductDesc = models.TextField(max_length=600, null=True, blank=True)
    ProductOrigin = models.CharField(max_length=100, null=True, blank=True)
    ProductManu = models.CharField(max_length=100, null=True, blank=True)
    ProductImage1 = models.ImageField(upload_to="Products", null=True, blank=True)
    ProductImage2 = models.ImageField(upload_to="Products", null=True, blank=True)
    ProductImage3 = models.ImageField(upload_to="Products", null=True, blank=True)
