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