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
    def __init__(self, *args, **kwargs):
        cloth_id = -1
        if 'cloth_id' in kwargs.keys():
            cloth_id = kwargs.pop('cloth_id')
        super(ClothForm, self).__init__(*args, **kwargs)

        cloth_code_value = ''
        cloth_name_value = ''
        used_for_value = ''
        breadth_value = 150
        grams_per_m2_value = ''
        category_name_value = ''
        texture_name_value = ''
        material_name_value = ''
        description_value = ''

        cloth = Cloth.objects.filter(pk=cloth_id).first()
        if cloth:
            if cloth.cloth_code:
                cloth_code_value = cloth.cloth_code
            if cloth.cloth_name:
                cloth_name_value = cloth.cloth_name
            if cloth.used_for:
                used_for_value = cloth.used_for
            if cloth.breadth:
                breadth_value = cloth.breadth
            if cloth.grams_per_m2:
                grams_per_m2_value = cloth.grams_per_m2
            if cloth.category:
                category_name_value = cloth.category
            if cloth.texture:
                texture_name_value = cloth.texture
            if cloth.material:
                material_name_value = cloth.material
            if cloth.description:
                description_value = cloth.description

        category_list = tuple(CategoryOfCloth.objects.all().values_list('category_name', flat=True))
        texture_list = tuple(TextureOfCloth.objects.all().values_list('texture_name', flat=True))
        material_list = tuple(MaterialOfCloth.objects.all().values_list('material_name', flat=True))

        self.fields['cloth_code'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '编号', 'value': cloth_code_value})

        self.fields['cloth_name'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '名称', 'value': cloth_name_value})

        self.fields['used_for'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '用途', 'value': used_for_value})

        self.fields['breadth'].widget = forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': '0', 'value': breadth_value})

        self.fields['grams_per_m2'].widget = forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': '0', 'value': grams_per_m2_value})

        self.fields['category_name'].widget = DataListWidget(category_list, 'category_name',
                                                             attrs={'class': 'form-control', 'placeholder': '分类',
                                                                    'value': category_name_value})

        self.fields['texture_name'].widget = DataListWidget(texture_list, 'texture_name',
                                                            attrs={'class': 'form-control', 'placeholder': '纹理',
                                                                   'value': texture_name_value})

        self.fields['material_name'].widget = DataListWidget(material_list, 'material_list',
                                                             attrs={'class': 'form-control', 'placeholder': '材质',
                                                                    'value': material_name_value})

        if cloth_id != -1:
            del self.fields["image"]
        else:
            self.fields['image'].widget = forms.ClearableFileInput(attrs={'class': 'form-control ', 'multiple': True})

        self.fields['description'].widget = forms.Textarea(
            attrs={'class': 'form-control', 'rows': 9, 'placeholder': '添加详细信息', 'value': description_value})

    cloth_code = forms.CharField(label='编号', max_length=20)
    cloth_name = forms.CharField(label='名称', max_length=20, required=False)
    used_for = forms.CharField(label='用途', max_length=100, required=False)
    breadth = forms.IntegerField(label='幅宽(cm)', required=False)
    grams_per_m2 = forms.IntegerField(label='克重', required=False)
    category_name = forms.CharField(label='分类', required=False)
    texture_name = forms.CharField(label='纹理', required=False)
    material_name = forms.CharField(label='材质', required=False)
    image = forms.FileField(label='图片', required=False)
    description = forms.CharField(label='详细信息', max_length=1000, required=False)


class OrderForm(forms.Form):
    serial_no = forms.CharField(
        label='单号',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '单号'}),
        max_length=20,
    )
