from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import product.models
import django.utils.timezone

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL), ("product", "0001_initial")]
    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("email", models.EmailField(default="", max_length=254, verbose_name="email")),
                ("status", models.CharField(choices=[("pending", "Pending"), ("paid", "Paid"), ("cancelled", "Cancelled")], default="pending", max_length=12, verbose_name="status")),
                ("total", models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name="total")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name="created at")),
                ("user", models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="orders", to=settings.AUTH_USER_MODEL, verbose_name="user")),
            ],
            options={
                "verbose_name": "order",
                "verbose_name_plural": "orders",
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("product_name", models.CharField(default="", max_length=160, verbose_name="product name")),
                ("unit_price", models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name="unit price")),
                ("quantity", models.PositiveIntegerField(default=1, verbose_name="quantity")),
                ("order", models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name="items", to="order.order", verbose_name="order")),
                ("product", models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to="product.product", verbose_name="product")),
            ],
            options={
                "verbose_name": "order item",
                "verbose_name_plural": "order items",
            },
        ),
    ]
