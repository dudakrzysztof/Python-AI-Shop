from decimal import Decimal
from django.db import transaction
from product.models import Product
from .models import Order, OrderItem
from .payment import ManualPaymentProvider, PaymentProvider

class StockError(ValueError):
    pass

@transaction.atomic
def create_order(*, email: str, cart: dict[str, int], user=None,
                 payment: PaymentProvider | None = None) -> Order:
    if not cart:
        raise ValueError("Cart is empty")
    products = list(Product.objects.select_for_update().filter(active=True, id__in=cart))
    by_id = {str(p.id): p for p in products}
    if len(by_id) != len(cart):
        raise StockError("One or more products are unavailable")
    total = Decimal("0")
    order = Order.objects.create(email=email, user=user, total=0)
    for key, quantity in cart.items():
        product = by_id[key]
        if quantity < 1 or quantity > product.stock:
            raise StockError(f"Insufficient stock for {product.name}")
        OrderItem.objects.create(order=order, product=product, product_name=product.name,
                                 unit_price=product.price, quantity=quantity)
        product.stock -= quantity
        product.save(update_fields=["stock", "updated_at"])
        total += product.price * quantity
    order.total = total
    result = (payment or ManualPaymentProvider()).charge(total, email)
    if not result.success:
        raise ValueError(result.message or "Payment failed")
    order.status = Order.Status.PAID
    order.save(update_fields=["total", "status"])
    return order
