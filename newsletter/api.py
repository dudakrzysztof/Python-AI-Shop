from ninja import Router, Schema
from .models import Subscriber
router = Router()
class EmailIn(Schema):
    email: str
@router.post("/subscribe")
def subscribe(request, payload: EmailIn):
    subscriber, _ = Subscriber.objects.update_or_create(email=payload.email, defaults={"subscribed": True})
    return {"email": subscriber.email, "subscribed": subscriber.subscribed}
@router.post("/unsubscribe")
def unsubscribe(request, payload: EmailIn):
    Subscriber.objects.filter(email=payload.email).update(subscribed=False)
    return {"email": payload.email, "subscribed": False}
