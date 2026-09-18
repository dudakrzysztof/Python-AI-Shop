from ninja import Router, Schema
from .services import create_order
router = Router()

class CartIn(Schema):
    email: str
    items: dict[str, int]

@router.post("/orders")
def make_order(request, payload: CartIn):
    order = create_order(email=payload.email, cart=payload.items)
    return {"id": order.id, "status": order.status, "total": order.total}

@router.get("/")
def cart(request):
    return {"items": request.session.get("cart", {})}
