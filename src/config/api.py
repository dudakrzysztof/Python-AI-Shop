from ninja import NinjaAPI
from product.api import router as product_router
from order.api import router as order_router
from newsletter.api import router as newsletter_router

api = NinjaAPI(title="Shop API", version="1.0")
api.add_router("/products", product_router)
api.add_router("/cart", order_router)
api.add_router("/newsletter", newsletter_router)
