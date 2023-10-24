from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Order
from django.urls import reverse
from django.contrib import messages
import json


# Create your views here.
def index(request):
    context = {}

    # for search result
    prod_search = request.GET.get('prod_search')
    if prod_search is not None and len(prod_search) > 0:
        all_products = Product.objects.filter(title__icontains=prod_search)
    else:
        # normal all products display
        all_products = Product.objects.all()

    if request.GET.get('order_success') == 'true':
        context['clear_cart'] = True

    paginator = Paginator(all_products, 16)
    page = request.GET.get('page')
    all_products = paginator.get_page(page)

    context["product_objects"] = all_products
    return render(request, template_name='shop/index.html',context=context)


# detail view of product
def detail(request, prod_id):
    try:
        product = Product.objects.get(pk=prod_id)
    except:
        messages.error(request, "Product not found!")
        return redirect('index')
    return render(request, 'shop/product.html', context={"product":product})



def checkout(request):
    if request.method == "POST":
        fields = ["name", "email", "address", "city", "state", "zipcode"]

        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipcode = request.POST.get("zipcode")
        items = request.POST.get("items")

        try:
            items = json.loads(items)

            total_value = 0

            for item_id in items:
                item = Product.objects.get(pk=int(item_id))
                total_value += item.discount_price

            if total_value <= 0:
                raise Exception("invalid order data")

            order = Order(name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, items=items, total_value=total_value)
            order.save()

            messages.success(request, f'Order placed successfully successfully.')

            url = reverse('index') + f'?order_success=true'
            return redirect(url)
        except:
            messages.error(request, "Invalid order data. Try ordering again. If issue persists, clear your cart and add items again.")
            return redirect('index')

    return render(request, 'shop/checkout.html')

