from django.contrib import admin

from Shop.models import Product, Order, OrderUpdate
from Shop.models import Order, OrderUpdate
from Shop.models import OrderUpdate
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderUpdate)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('prod_name','prod_desc','pub_date')