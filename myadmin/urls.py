from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="Home"),
    path('checkout', views.checkout, name='CheckOut'),
    path('products/<int:id>', views.product_view, name='Product_View'),
    path('track_order', views.tracker, name='Tracker'),
]