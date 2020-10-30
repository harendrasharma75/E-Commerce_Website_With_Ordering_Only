from django.shortcuts import render, redirect, HttpResponse
from Shop.models import Product, Order, OrderUpdate
from math import ceil
import json
# Create your views here.


def index(request):
    allprods = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat,status="Active")
        if len(prod)==0:
            continue
        n = len(prod)
        nSlides = n//4 +ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])

    context = {
        'allprods':allprods
    }
    return render(request, 'index.html',context)


def checkout(request):
    id = None
    thank=False
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('pin_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json,amount=amount,email=email, name=name, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone,order_status='Pending',delivery_status='Pending')
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})        
    
    context = {
        'thank':thank, 
        'id': id
    }
    return render(request,'checkout.html',context)

def product_view(request,id):
   
    product = Product.objects.filter(id=id)
    
    context = {
        'product':product[0],
    }
    return render(request,'product_veiw.html',context)


def tracker(request):
    response = {}
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        mobile = request.POST.get('mobile', '')
        try:
            order = Order.objects.filter(order_id=orderId)
    
            if len(order)>0 and order[0].phone == mobile:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    # response = json.dumps([updates, order[0].items_json], default=str)
                    # print(response)
                    items = json.loads(order[0].items_json)
                    response = {
                        'updates':updates,
                        'items':items,
                        'order':order[0],
                    }
                # return HttpResponse(response)
            else:
                response = {
                    'msg':'Order Id or Mobile Number is incorrect. Please try again with correct details.'
                }
        except Exception as e:
            return HttpResponse('{}')


    return render(request, 'tracker.html', response)