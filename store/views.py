from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def store(request, category_slug=None):
    
    if category_slug != None:
        products = Product.objects.all().filter(is_available=True, category__slug=category_slug)
    else:
        products = Product.objects.all().filter(is_available=True)

    products_count = products.count()

    context = {'products': products, 'products_count': products_count}

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    
    context = {'product': product}

    return render(request, 'store/product-detail.html', context)