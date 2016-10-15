from django.forms import ModelForm

from .models import Order


class SalesListForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['']
