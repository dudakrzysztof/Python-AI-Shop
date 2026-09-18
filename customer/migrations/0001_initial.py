from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [migrations.CreateModel(
        name="CustomerProfile",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("phone", models.CharField(blank=True, default="", max_length=40, verbose_name="phone")),
            ("address", models.TextField(blank=True, default="", verbose_name="address")),
            ("user", models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name="customer_profile", to=settings.AUTH_USER_MODEL, verbose_name="user")),
        ],
        options={
            "verbose_name": "customer profile",
            "verbose_name_plural": "customer profiles",
        },
    )]
