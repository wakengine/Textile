from django.forms import ModelForm

from .models import SalesList


class SalesListForm(ModelForm):
    class Meta:
        model = SalesList
        exclude = ['']
