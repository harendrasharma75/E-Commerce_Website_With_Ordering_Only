from django.shortcuts import render, redirect
from Shop.models import Product
from Shop.models import Order
from Shop.models import OrderUpdate
from Shop.forms import UpdateProduct
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
# Create your views here.

def adminlogin(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        user = auth.authenticate(username=user_id,password=password)
        
        if user is not None:
            auth.login(request,user)
            if request.GET.get('next',None):
                return redirect(request.GET['next'])

            return redirect('Add_Product','new')
            

    return render(request,'adminlogin.html')

@login_required(login_url='/mysuperadmin')
def admin_page(request,id):
    if id == "new":
        item = None
    else:
        item = Product.objects.get(id=id)

    products = Product.objects.all()

    if request.method=="POST":
        id = request.POST.get("id")
        if id == "":
            prod = UpdateProduct(request.POST,request.FILES)
            if prod.is_valid():
                prod.save()
           
        else:
            item = Product.objects.get(id=id)
            print(item.prod_name)
            prod = UpdateProduct(request.POST,request.FILES, instance = item)
            if prod.is_valid():
                prod.save()
        item = None

    context = {
        'products':products,

        'item':item,
    }
    return render(request,'addproducts.html',context)

@login_required(login_url='/mysuperadmin')
def pending_order(request,id):

    if id=="None":
        search = None
    else:
        search = Order.objects.get(order_id=id)
    
    if request.method=="POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        remarks = request.POST.get("remarks")
        order_status = request.POST.get("order_status")
        delivery_status = request.POST.get("delivery_status")

        search = Order.objects.filter(order_id=id,phone=mobile)
        if len(search)>0:
            search = Order.objects.get(order_id=id,phone=mobile)
            search.order_status = order_status
            search.delivery_status = delivery_status
            search.remarks=remarks
            search.save()

            if order_status == 'Accepted' and remarks != "" and delivery_status != 'Delivered':
                update = OrderUpdate(order_id=id, update_desc=remarks)
                update.save()
            
            if delivery_status == 'Delivered':
                remark = "Your Order has been delivered successfully"
                search.delivery_date = datetime.now()
                search.remarks = remark
                search.save()
                update = OrderUpdate(order_id=id, update_desc=remark)
                update.save()

            search = None
            
    pendings = Order.objects.filter(delivery_status='Pending')
    delivered = Order.objects.filter(delivery_status='Delivered')
    rejected = Order.objects.filter(delivery_status='Rejected')

    context = {
        'search':search,
        'pendings':pendings,
        'delivered':delivered,
        'rejected':rejected,
    }
    return render(request,'pending_order.html',context)

def logout(request):
    auth.logout(request)
    return redirect('Admin')