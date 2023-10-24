from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=500)


    def __str__(self) -> str:
        return self.title



class Order(models.Model):
    items = models.CharField(max_length=10000)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    total_value = models.FloatField()

    def __str__(self) -> str:
        return self.email