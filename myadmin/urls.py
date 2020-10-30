from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminlogin, name="Admin"),
    path('update_<id>',views.admin_page, name="Add_Product"),
    path('pending_order_<id>',views.pending_order, name="Pending_Order"),
    path('logout', views.logout, name='Logout'),
]