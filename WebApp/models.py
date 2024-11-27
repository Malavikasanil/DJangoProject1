from django.db import models

# Create your models here.
class Contacts(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Contact = models.IntegerField(null=True, blank=True)
    Comment = models.TextField(max_length=400, null=True, blank=True)

class Signup(models.Model):
    UName = models.CharField(max_length=100, null=True, blank=True)
    UContact = models.IntegerField(null=True, blank=True)
    UEmail = models.EmailField(max_length=100, null=True, blank=True)
    UPass = models.CharField(max_length=100, null=True, blank=True)
    URPass = models.CharField(max_length=100, null=True, blank=True)

class Cart(models.Model):
    PQuantity = models.IntegerField(null=True, blank=True)
    PPrice = models.IntegerField(null=True, blank=True)
    PName = models.CharField(max_length=200, null=True, blank=True)
    Total = models.IntegerField(null=True, blank=True)
    UName = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to='cartProduct/', null=True, blank=True)

class Order(models.Model):
    UName = models.CharField(max_length=100, null=True, blank=True)
    UMail = models.EmailField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Addr = models.CharField(max_length=300, null=True, blank=True)
    Town = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.IntegerField(null=True, blank=True)
    Contact = models.IntegerField(null=True, blank=True)
    Comment = models.TextField(max_length=400, null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)