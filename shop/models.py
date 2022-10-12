# from itertools import product
from django.db import models

# Create your models here.
class Product(models.Model):
    pruduct_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50 , default="")
    subcategory = models.CharField(max_length=50 , default="")
    desc = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images" ,default="")

# For call the product name make this method within same class
    def __str__(Self):
         return Self.product_name



