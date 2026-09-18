from decimal import Decimal
from ninja import Router, Schema
from .models import Product

router = Router()

class ProductOut(Schema):
    id: int
    name: str
    slug: str
    description: str
    price: Decimal
    stock: int

@router.get("/", response=list[ProductOut])
def products(request):
    return Product.objects.filter(active=True)

@router.get("/{slug}", response=ProductOut)
def product(request, slug: str):
    return Product.objects.get(slug=slug, active=True)
