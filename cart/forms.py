from django.forms import Form, ModelForm, BooleanField, HiddenInput, TypedChoiceField
from shop.models import Warehouse


class CartAddProductForm(Form):
    update = BooleanField(required=False, initial=False, widget=HiddenInput)
