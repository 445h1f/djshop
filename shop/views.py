from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product


# Create your views here.
def index(request):

    # for search result
    prod_search = request.GET.get('prod_search')
    if prod_search is not None and len(prod_search) > 0:
        all_products = Product.objects.filter(title__icontains=prod_search)
    else:
        # normal all products display
        all_products = Product.objects.all()

    paginator = Paginator(all_products, 16)
    page = request.GET.get('page')
    all_products = paginator.get_page(page)

    return render(request, template_name='shop/index.html',context={"product_objects" : all_products})


# detail view of product
def detail(request, prod_id):
    try:
        product = Product.objects.get(pk=prod_id)
    except:
        return render(request, 'shop/404.html')
    return render(request, 'shop/product.html', context={"product":product})


# checkout page
def checkout(request):
    cart_data_raw = request.POST.get('cart_data')

    if cart_data_raw:
        if cart_data_raw[-1] == ',':
            cart_data_raw = cart_data_raw[:-1]
        # filtering data
        items_data = cart_data_raw.split(',')

        cart_data = []

        total_price = 0
        total_discount_price = 0
        total_quantity = 0

        for item in items_data:
            item = item.split(':')
            item_id = int(item[0].strip())
            item_quantity = int(item[1].strip());
            print(item_id, item_quantity)
            prod = Product.objects.get(pk=item_id)
            product_data = {
                "id" : prod.pk,
                "title" : prod.title,
                "price": prod.price,
                "discount_price" : prod.discount_price,
                "image" : prod.image,
                "quantity": item_quantity,
            }
            total_price += prod.price
            total_discount_price += prod.discount_price

            total_quantity += item_quantity
            cart_data.append(product_data)

        order_info = {
            "total_discount_price" : total_discount_price,
            "total_price" : total_price,
            "savings" : total_price - total_discount_price,
            "total_quantity" : total_quantity
        }
        return render(request, 'shop/checkout.html', context={"cart_data" : cart_data, "order_info": order_info})

    return render(request, 'shop/checkout.html')
