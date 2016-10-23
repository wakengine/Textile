from utils.form_utils import *


class OrderForm(forms.Form):
    serial_no = forms.CharField(
        label='单号',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '单号'}),
        max_length=20)
