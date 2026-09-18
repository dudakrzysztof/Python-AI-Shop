from django.core.management.base import BaseCommand
from product.models import Product

class Command(BaseCommand):
    help = "Create a few safe demo products."
    def handle(self, *args, **options):
        examples = [("Canvas tote", "canvas-tote", "A durable everyday tote.", "24.00", 20),
                    ("Desk mug", "desk-mug", "A simple ceramic mug.", "16.00", 30)]
        for name, slug, description, price, stock in examples:
            Product.objects.update_or_create(slug=slug, defaults={"name": name, "description": description,
                "price": price, "stock": stock, "active": True})
        self.stdout.write(self.style.SUCCESS("Demo products ready."))
