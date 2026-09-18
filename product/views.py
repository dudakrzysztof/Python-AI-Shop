from django.shortcuts import get_object_or_404, render
from .forms import AddToCartForm
from .models import Product

def home(request):
    return render(request, "home.html", {"products": Product.objects.filter(active=True)})

def product_list(request):
    return render(request, "product/list.html", {"products": Product.objects.filter(active=True)})

def product_detail(request, slug: str):
    product = get_object_or_404(Product, slug=slug, active=True)
    return render(request, "product/detail.html", {"product": product, "form": AddToCartForm()})
