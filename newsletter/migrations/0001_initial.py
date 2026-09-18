from django.db import migrations, models
import django.utils.timezone
class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(
        name="Subscriber",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("email", models.EmailField(default="", max_length=254, unique=True, verbose_name="email")),
            ("subscribed", models.BooleanField(default=True, verbose_name="subscribed")),
            ("created_at", models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name="created at")),
            ("updated_at", models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name="updated at")),
        ],
        options={
            "verbose_name": "newsletter subscriber",
            "verbose_name_plural": "newsletter subscribers",
        },
    )]
