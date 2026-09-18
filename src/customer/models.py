from django.conf import settings
from django.db import models


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        on_delete=models.CASCADE,
        related_name="customer_profile",
        blank=False,
        null=False,
        default=None,
    )
    phone = models.CharField(
        verbose_name="phone",
        max_length=40,
        blank=True,
        null=False,
        default="",
    )
    address = models.TextField(
        verbose_name="address",
        blank=True,
        null=False,
        default="",
    )

    class Meta:
        app_label = "customer"
        verbose_name = "customer profile"
        verbose_name_plural = "customer profiles"

    def __str__(self) -> str:
        return self.user.get_username()
