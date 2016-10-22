from django import forms
from django.template.loader_tags import register

from asset.models import Company


@register.filter(name='is_textarea')
def is_textarea(field):
    return field.field.widget.__class__.__name__ == forms.Textarea().__class__.__name__


class CompanyForm(forms.Form):
    name = forms.CharField(label='公司名', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '公司名'}), max_length=20)
    owner_name = forms.CharField(label='所有者', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '所有者'}), max_length=20)
    description = forms.CharField(label='详细信息', max_length=20,
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control', 'rows': 9, 'placeholder': '添加详细信息'}),
                                  required=False)

    relationship = forms.ChoiceField(label='关系', choices=Company.RelationShip, widget=forms.Select(
        attrs={'class': 'form-control', }))

    CHECKBOX_CHOICES = (('C', 'Customer'), ('S', 'Supplier'))
    is_customer = forms.MultipleChoiceField(required=False,
                                            widget=forms.CheckboxSelectMultiple(),
                                            choices=CHECKBOX_CHOICES)

    is_a = forms.BooleanField(label='Customer', required=False)
    image = forms.FileField(label='图片', required=False)
