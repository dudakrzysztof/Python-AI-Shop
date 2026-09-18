from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from product.models import Product


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PAID = "paid", "Paid"
        CANCELLED = "cancelled", "Cancelled"

    user = models.ForeignKey(
        get_user_model(),
        verbose_name="user",
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="orders",
    )
    email = models.EmailField(
        verbose_name="email",
        blank=False,
        null=False,
        default="",
    )
    status = models.CharField(
        verbose_name="status",
        max_length=12,
        choices=Status.choices,
        blank=False,
        null=False,
        default=Status.PENDING,
    )
    total = models.DecimalField(
        verbose_name="total",
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        default=Decimal("0"),
    )
    created_at = models.DateTimeField(
        verbose_name="created at",
        blank=False,
        null=False,
        default=timezone.now,
        editable=False,
    )

    class Meta:
        app_label = "order"
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self) -> str:
        return f"Order #{self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name="order",
        on_delete=models.CASCADE,
        related_name="items",
        blank=False,
        null=False,
        default=None,
    )
    product = models.ForeignKey(
        Product,
        verbose_name="product",
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        default=None,
    )
    product_name = models.CharField(
        verbose_name="product name",
        max_length=160,
        blank=False,
        null=False,
        default="",
    )
    unit_price = models.DecimalField(
        verbose_name="unit price",
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        default=Decimal("0"),
    )
    quantity = models.PositiveIntegerField(
        verbose_name="quantity",
        blank=False,
        null=False,
        default=1,
    )

    class Meta:
        app_label = "order"
        verbose_name = "order item"
        verbose_name_plural = "order items"

    @property
    def subtotal(self) -> Decimal:
        return self.unit_price * self.quantity
