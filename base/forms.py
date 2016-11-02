from utils.form_utils import *


class EntityForm(forms.Form):
    entity_name = forms.CharField(
        label='单位名',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '单位名'}),
        max_length=20,
    )

    RelationShip = (
        ('C', 'Customer'),
        ('S', 'Supplier'),
        ('B', 'Both'),
    )
    relationship = forms.ChoiceField(
        label='关系',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=RelationShip,
    )

    country_list = ('Mexico', 'USA', 'China', 'France')
    my_data_list = forms.CharField(
        label='数据表测试',
        widget=DataListWidget(country_list, 'my_data_list', attrs={'class': 'form-control', 'placeholder': '数据表'}),
    )

    number_field = forms.FloatField(
        label='数字测试',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': 'any', 'placeholder': '0.0'}),
    )

    data_field = forms.DateField(
        label='日期测试',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )

    description = forms.CharField(
        label='详细信息',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 9, 'placeholder': '添加详细信息'}),
        max_length=20,
        required=False,
    )

    CHECKBOX_CHOICES = (('1', '选项1'), ('2', '选项2'), ('3', '选项3'))
    multi_choice = forms.MultipleChoiceField(
        label='多选测试',
        widget=forms.CheckboxSelectMultiple(),
        choices=CHECKBOX_CHOICES,
        required=False,
    )

    check_box = forms.BooleanField(
        label='勾选框测试',
        widget=forms.CheckboxInput(attrs={'class': 'checkbox', 'style': 'min-width: 16px'}),
        required=False,
    )

    image = forms.ImageField(
        label='图片',
        required=False,
    )


class ClothForm(forms.Form):
    serial_no = forms.CharField(
        label='编号',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '编号'}),
        max_length=20,
    )

    name = forms.CharField(
        label='名称',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名称'}),
        max_length=20,
    )
