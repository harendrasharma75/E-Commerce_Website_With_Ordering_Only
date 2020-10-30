
from django import forms  
from django.contrib.auth.models import User
from Shop.models import Product



class UpdateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prod_name','category','sub_category','price','prod_desc','status','prod_image']