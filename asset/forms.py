from django import forms
from django.template.loader_tags import register

from asset.models import Company


@register.filter(name='is_textarea')
def is_textarea(field):
    return field.field.widget.__class__.__name__ == forms.Textarea().__class__.__name__


@register.filter(name='is_checkbox')
def is_textarea(field):
    return field.field.widget.__class__.__name__ == forms.CheckboxInput().__class__.__name__


class DataListWidget(forms.TextInput):
    def __init__(self, data_list, name, *args, **kwargs):
        super(DataListWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list': 'list_{}'.format(self._name)})

    def render(self, name, value, attrs=None):
        text_html = super(DataListWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list_{}">'.format(self._name)
        for item in self._list:
            data_list += '<option value="{}">'.format(item)
        data_list += '</datalist>'

        return text_html + data_list


class CompanyForm(forms.Form):
    name = forms.CharField(
        label='公司名',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '公司名'}),
        max_length=20)

    owner_name = forms.CharField(
        label='所有者',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '所有者'}),
        max_length=20)

    relationship = forms.ChoiceField(
        label='关系',
        widget=forms.Select(attrs={'class': 'form-control', }),
        choices=Company.RelationShip)

    country_list = ('Mexico', 'USA', 'China', 'France')
    my_data_list = forms.CharField(
        label='数据表测试',
        widget=DataListWidget(country_list, 'my_data_list', attrs={'class': 'form-control', 'placeholder': '数据表'}))

    number_field = forms.FloatField(
        label='数字测试',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': 'any', 'placeholder': '0.0'})
    )

    data_field = forms.DateField(
        label='日期测试',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    description = forms.CharField(
        label='详细信息',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 9, 'placeholder': '添加详细信息'}),
        max_length=20,
        required=False)

    CHECKBOX_CHOICES = (('1', '选项1'), ('2', '选项2'), ('3', '选项3'))
    multi_choice = forms.MultipleChoiceField(
        label='多选测试',
        widget=forms.CheckboxSelectMultiple(),
        choices=CHECKBOX_CHOICES,
        required=False)

    check_box = forms.BooleanField(
        label='勾选框测试',
        widget=forms.CheckboxInput(attrs={'class': 'checkbox', 'style': 'min-width: 16px'}),
        required=False, )

    image = forms.ImageField(
        label='图片',
        required=False)
