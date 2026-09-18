from django.db import models

from django.utils import timezone


class Subscriber(models.Model):
    email = models.EmailField(
        verbose_name="email",
        unique=True,
        blank=False,
        null=False,
        default="",
    )
    subscribed = models.BooleanField(
        verbose_name="subscribed",
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
        app_label = "newsletter"
        verbose_name = "newsletter subscriber"
        verbose_name_plural = "newsletter subscribers"

    def save(self, *args: object, **kwargs: object) -> None:
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email
