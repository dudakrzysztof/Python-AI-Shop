from django.urls import path
from .views import add_to_cart, cart_view, checkout
urlpatterns = [path("", cart_view, name="cart"), path("add/<int:product_id>/", add_to_cart, name="add-to-cart"),
               path("checkout/", checkout, name="checkout")]
