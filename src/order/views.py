from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CheckoutForm
from .services import StockError, create_order
from product.models import Product

def cart_view(request):
    cart = request.session.get("cart", {})
    products = Product.objects.filter(id__in=cart, active=True)
    rows = [{"product": p, "quantity": int(cart[str(p.id)]), "subtotal": p.price * int(cart[str(p.id)])} for p in products]
    return render(request, "order/cart.html", {"rows": rows, "total": sum((r["subtotal"] for r in rows), 0)})

def add_to_cart(request, product_id: int):
    if request.method == "POST":
        quantity = max(1, int(request.POST.get("quantity", 1)))
        cart = request.session.setdefault("cart", {})
        key = str(product_id)
        cart[key] = int(cart.get(key, 0)) + quantity
        request.session.modified = True
    return redirect("cart")

def checkout(request):
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                order = create_order(email=form.cleaned_data["email"], cart=request.session.get("cart", {}),
                                     user=request.user if request.user.is_authenticated else None)
            except (ValueError, StockError) as exc:
                form.add_error(None, str(exc))
            else:
                request.session["cart"] = {}
                return render(request, "order/success.html", {"order": order})
    else:
        form = CheckoutForm()
    return render(request, "order/checkout.html", {"form": form})
