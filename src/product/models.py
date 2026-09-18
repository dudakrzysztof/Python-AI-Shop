from decimal import Decimal
from django.utils import timezone
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(
        verbose_name="name",
        max_length=160,
        blank=False,
        null=False,
        default="",
    )
    slug = models.SlugField(
        verbose_name="slug",
        unique=True,
        blank=False,
        null=False,
        default="",
    )
    description = models.TextField(
        verbose_name="description",
        blank=True,
        null=False,
        default="",
    )
    price = models.DecimalField(
        verbose_name="price",
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        default=Decimal("0"),
    )
    stock = models.PositiveIntegerField(
        verbose_name="stock",
        blank=False,
        null=False,
        default=0,
    )
    active = models.BooleanField(
        verbose_name="active",
        blank=False,
        null=False,
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name="created at",
        blank=False,
        null=False,
        default=timezone.now,
        editable=False,
    )
    updated_at = models.DateTimeField(
        verbose_name="updated at",
        blank=False,
        null=False,
        default=timezone.now,
        editable=False,
    )

    class Meta:
        app_label = "product"
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ["name"]

    def save(self, *args: object, **kwargs: object) -> None:
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("product-detail", kwargs={"slug": self.slug})

    @property
    def in_stock(self) -> bool:
        return self.stock > 0
