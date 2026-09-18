from django import forms
from .models import Product

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=99, initial=1)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "slug", "description", "price", "stock", "active")
