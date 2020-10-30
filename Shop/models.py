from django.db import models
from datetime import date
# Create your models here.


class Product(models.Model):
    prod_id = models.AutoField
    prod_name = models.CharField(max_length=50,blank=True)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    prod_desc = models.CharField(max_length=300,blank=True)
    pub_date = models.DateField(auto_now_add=True)
    prod_image = models.ImageField(upload_to="Shop",blank=True)
    status = models.CharField(max_length=20,blank=True)



class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=90)
    amount = models.IntegerField(default=0)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, blank=True)
    delivery_status = models.CharField(max_length=20, blank=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True)


class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)