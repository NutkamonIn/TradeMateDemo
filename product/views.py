from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):
    all_products = Product.objects.all()
    context = { 'products': all_products }
    return render(request,"product/products.html",context)

def product(request, product_id):
    one_product = Product.objects.get(id=product_id)
    context = { 'product': one_product}
    return render(request,"product/product.html", context)
