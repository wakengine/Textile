from .form_base import *
from .models import *


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
    category_list = tuple(CategoryOfCloth.objects.all().values_list('category_name', flat=True))
    texture_list = tuple(TextureOfCloth.objects.all().values_list('texture_name', flat=True))
    material_list = tuple(MaterialOfCloth.objects.all().values_list('material_name', flat=True))

    cloth_code = forms.CharField(
        label='编号',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '编号'}),
        max_length=20,
    )

    cloth_name = forms.CharField(
        label='名称',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名称'}),
        max_length=20,
        required=False,
    )

    breadth = forms.IntegerField(
        label='幅宽(cm)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0', 'value': '150'}),
        required=False,
    )

    used_for = forms.CharField(
        label='用途',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用途'}),
        max_length=100,
        required=False,
    )

    grams_per_m2 = forms.IntegerField(
        label='克重',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        required=False,
    )

    category_name = forms.CharField(
        label='分类',
        widget=DataListWidget(category_list, 'category_name', attrs={'class': 'form-control', 'placeholder': '分类'}),
        required=False,
    )

    texture_name = forms.CharField(
        label='纹理',
        widget=DataListWidget(texture_list, 'texture_name', attrs={'class': 'form-control', 'placeholder': '纹理'}),
        required=False,
    )

    material_name = forms.CharField(
        label='材质',
        widget=DataListWidget(material_list, 'material_list', attrs={'class': 'form-control', 'placeholder': '材质'}),
        required=False,
    )

    description = forms.CharField(
        label='详细信息',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 9, 'placeholder': '添加详细信息'}),
        max_length=1000,
        required=False,
    )


class OrderForm(forms.Form):
    serial_no = forms.CharField(
        label='单号',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '单号'}),
        max_length=20,
    )
