from django.db import models

# Create your models here.

class Add_Products(models.Model):
    product_name = models.CharField(max_length=30)
    product_desc = models.TextField(max_length=100)
    product_price = models.IntegerField()


