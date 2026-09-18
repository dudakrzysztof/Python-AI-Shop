from django.contrib import admin
from django.urls import include, path
from product.views import home
from config.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("products/", include("product.urls")),
    path("cart/", include("order.urls")),
    path("newsletter/", include("newsletter.urls")),
    path("api/", api.urls),
]
