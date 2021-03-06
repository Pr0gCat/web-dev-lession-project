from django.urls import path
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect
import json

from .models import Shop, Item, ItemCategory, Order, OrderItem
from .forms import AddItemForm
from takoeats import models

def get_random_opened_shop(request):
    pass

"""
商店管理
"""
@login_required
def toggle_shop(request):
    """
    """
    if request.method == 'POST' and request.is_ajax():
        shop_id = request.POST.get('shop_id')
        shop = Shop.objects.get(id=shop_id)
        checked = request.POST.get('checked')
        if shop.owner != request.user:
            return JsonResponse({'status': 'faliure'})
        shop.opened = not shop.opened if checked is None else checked == 'true'
        print(shop.opened)
        shop.save()
        return JsonResponse({'status': 'success'})
    elif request.method == 'GET':
        shop_id = request.GET.get('shop_id')
        shop = Shop.objects.get(id=shop_id)
        if shop != None:
            return JsonResponse({'status': 'success', 'opened': shop.opened})
    return JsonResponse({'status': 'faliure'})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            print(form)
            #no validation
            print(request.POST)
            shop = Shop.objects.get(owner=request.user)
            category = ItemCategory.objects.filter(shop=shop, name=request.POST.get('category'))
            if category.exists():
                category = category.first()
            else:
                category = ItemCategory.objects.create(shop=shop, name=request.POST.get('category'))
            
            Item.objects.create(shop=shop, \
                name=request.POST.get('name'), \
                price=request.POST.get('price'), \
                desc=request.POST.get('desc'),\
                status=(0 if request.POST.get('status') else 1),\
                category=category,
                image=request.FILES.get('image')
                            )
    return redirect('/s')

@login_required
def item_status(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        checked = request.POST.get('checked')
        item = Item.objects.get(id=item_id)
        if item.shop.owner != request.user:
            return JsonResponse({'status': 'faliure'})
        item.status = checked
        item.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'faliure'})

@login_required
def create_order(request):
    if request.method == 'POST' and request.is_ajax():
        print(request.POST)
        items = request.POST.get('items')
        shop_id = request.POST.get('shop_id')
        if items is None:
            JsonResponse({'status': 'faliure'})
        items = json.loads(items).values()
        # create order
        address = models.User.objects.get(user_entity=request.user).address
        shop = Shop.objects.get(id=shop_id)
        
        order = Order.objects.create(shop=shop, customer=request.user, delivery=None, status=1, price_sum=0, address=address)
        price_sum = 0
        for item in items:
            item_id = item['id']
            item_quantity = item['quantity']
            item = Item.objects.get(id=item_id)
            price = item.price * item_quantity
            price_sum += price
            OrderItem.objects.create(order=order, item=item, quantity=item_quantity, price=price).save()
        order.price_sum = price_sum
        order.save()
        return JsonResponse({'status': 'success'})

def get_order(request):
    if request.method == 'GET':
        shop_id = request.GET.get('shop_id')
        if shop_id:
            shop = Shop.objects.get(id=shop_id)
            orders = Order.objects.filter(shop=shop).all()
            orders = orders.exclude(status=3)
            orders = orders.exclude(status=4)
            orders = orders.exclude(status=5)
            orders = orders.exclude(status=6)
        else:
            orders = Order.objects.filter(customer=request.user).all()
            orders = orders.exclude(status=6)
            orders = orders.exclude(status=5)
        orders_list = []
        for order in orders:
            items = OrderItem.objects.filter(order=order).all()
            o = {
                'id': order.id,
                'customer': models.User.objects.get(user_entity=order.customer).display_name,
                'status': order.status,
                'price_sum': order.price_sum,
                'order_time': order.order_time,
                'items': [{
                    'name': item.item.name,
                    'quantity': item.quantity,
                    'price': item.price
                } for item in items]
            }
            orders_list.append(o)
        return JsonResponse({'status': 'success', 'orders': orders_list})

def update_order(request):
    if request.method == 'POST' and request.is_ajax():
        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        if order.status < 6:
            order.status += 1
            order.save()
        return JsonResponse({'status': 'success'})

urlpatterns = [
    path('randshop', get_random_opened_shop, name='randshop'),
    path('toggleshop', toggle_shop, name='toggleshop'),
    path('additem', add_item, name='additem'),
    path('itemstatus', item_status, name='itemstatus'),
    path('createorder', create_order, name='createorder'),
    path('getorder', get_order, name='getorder'),
    path('updateorder', update_order, name='updateorder'),
]