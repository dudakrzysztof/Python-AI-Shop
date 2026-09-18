from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(
        name="Product",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(default="", max_length=160, verbose_name="name")),
            ("slug", models.SlugField(default="", unique=True, verbose_name="slug")),
            ("description", models.TextField(blank=True, default="", verbose_name="description")),
            ("price", models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name="price")),
            ("stock", models.PositiveIntegerField(default=0, verbose_name="stock")),
            ("active", models.BooleanField(default=True, verbose_name="active")),
            ("created_at", models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name="created at")),
            ("updated_at", models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name="updated at")),
        ],
        options={
            "verbose_name": "product",
            "verbose_name_plural": "products",
            "ordering": ["name"],
        },
    )]
