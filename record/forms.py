from .form_base import *
from .models import *


def fill_init_value(form, field_name, value):
    if value:
        form.fields[field_name].initial = value


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
    def __init__(self, *args, **kwargs):
        cloth_id = -1
        if 'cloth_id' in kwargs.keys():
            cloth_id = kwargs.pop('cloth_id')
        super(ClothForm, self).__init__(*args, **kwargs)

        cloth = Cloth.objects.filter(pk=cloth_id).first()
        if cloth:
            fill_init_value(self, 'cloth_code', cloth.cloth_code)
            fill_init_value(self, 'cloth_name', cloth.cloth_name)
            fill_init_value(self, 'used_for', cloth.used_for)
            fill_init_value(self, 'breadth', cloth.breadth)
            fill_init_value(self, 'grams_per_m2', cloth.grams_per_m2)
            fill_init_value(self, 'category_name', cloth.category)
            fill_init_value(self, 'texture_name', cloth.texture)
            fill_init_value(self, 'material_name', cloth.material)
            fill_init_value(self, 'description', cloth.description)

        category_list = tuple(CategoryOfCloth.objects.all().values_list('category_name', flat=True))
        texture_list = tuple(TextureOfCloth.objects.all().values_list('texture_name', flat=True))
        material_list = tuple(MaterialOfCloth.objects.all().values_list('material_name', flat=True))
        self.fields['category_name'].widget = DataListWidget(
            category_list, 'category_name', attrs={'class': 'form-control', 'placeholder': '分类'})
        self.fields['texture_name'].widget = DataListWidget(
            texture_list, 'texture_name', attrs={'class': 'form-control', 'placeholder': '纹理'})
        self.fields['material_name'].widget = DataListWidget(
            material_list, 'material_list', attrs={'class': 'form-control', 'placeholder': '材质'})

        if cloth_id != -1:
            del self.fields["image"]

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

    used_for = forms.CharField(
        label='用途',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用途'}),
        max_length=100,
        required=False,
    )

    breadth = forms.IntegerField(
        label='幅宽(cm)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        initial=150,
        required=False,
    )

    grams_per_m2 = forms.IntegerField(
        label='克重',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        required=False,
    )

    category_name = forms.CharField(
        label='分类',
        required=False,
    )

    texture_name = forms.CharField(
        label='纹理',
        required=False,
    )

    material_name = forms.CharField(
        label='材质',
        required=False,
    )

    image = forms.FileField(
        label='图片',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True}),
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
