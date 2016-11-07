import datetime
import os

from PIL import Image
from django.db import models


class EntityManager(models.Manager):
    """
    Manage BusinessEntity related models.
    """

    @staticmethod
    def create_entity_from_form_data(form):
        """
        Create an instance of Entity from form data
        :param form: Form data posted by user
        :return: An instance of Entity
        """
        entity = BusinessEntity()
        entity.entity_name = form['entity_name']
        return entity


class ClothManager(models.Manager):
    @staticmethod
    def create_cloth_from_form_data(form, pk=-1):
        """
        Create an instance of Cloth from form data
        :param form: Form data posted by user
        :param pk: Primary key of the cloth
        :return: An instance of Cloth
        """
        if pk == -1:
            cloth = Cloth()
        else:
            cloth = Cloth.objects.filter(pk=pk).first()

        cloth.cloth_code = form['cloth_code']
        cloth.cloth_name = form['cloth_name']
        cloth.breadth = form['breadth']
        cloth.grams_per_m2 = form['grams_per_m2']
        cloth.used_for = form['used_for']
        cloth.description = form['description']

        category = form['category_name']
        material = form['material_name']
        texture = form['texture_name']

        if category:
            category, _ = CategoryOfCloth.objects.update_or_create(category_name=category)
            cloth.category = category
        if material:
            material, _ = MaterialOfCloth.objects.update_or_create(material_name=material)
            cloth.material = material
        if texture:
            texture, _ = TextureOfCloth.objects.update_or_create(texture_name=texture)
            cloth.texture = texture

        if not cloth.cloth_name:
            cloth.cloth_name = cloth.cloth_code

        return cloth


class StockManager(models.Manager):
    @staticmethod
    def create_inventory_from_form_data(form):
        """
        Create an instance of Inventory from form data
        :param form: Form data posted by user
        :return: An instance of Inventory
        """
        inventory = Inventory()
        inventory.roll_of_cloth = RollOfCloth()
        return inventory


class OrderManager(models.Manager):
    @staticmethod
    def create_order_from_form_data(form):
        """Create an instance of Order from form data
        :param form: Form data posted by user
        :return: An instance of Order
        """
        order = Order()
        order.serial_no = form['serial_no']
        return order

    def get_total_price(self):
        total_price = 0.0
        all_list = self.all()
        for item in all_list:
            total_price += item.total_price

        return format(total_price, ',')


class ImageBase(models.Model):
    """
    Base image class, may be used by any model.
    """
    IMAGE_DIR = 'images/'

    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.FileField()
    thumbnail = models.FileField()
    description = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def create_image_from_form(self, src_file, abs_dir):
        base_name = str(datetime.datetime.today()).replace(' ', '_').replace(':', '-')
        img_main = '{}/{}.jpg'.format(self.IMAGE_DIR, base_name)
        img_thumbnail = '{}/{}.thumb.jpg'.format(self.IMAGE_DIR, base_name)

        main_file = os.path.join(abs_dir, img_main)
        os.makedirs(os.path.dirname(main_file), exist_ok=True)
        with open(main_file, 'wb+') as dst:
            for chunk in src_file.chunks():
                dst.write(chunk)

        try:
            f = open(main_file, 'rb')
            img = Image.open(f)
            size = 256, 256
            img.thumbnail(size)
            img.save(os.path.join(abs_dir, img_thumbnail), 'JPEG')
            f.close()
        except IOError:
            f.close()
            os.remove(main_file)
            raise TypeError('Not a valid image')

        self.image = img_main
        self.thumbnail = img_thumbnail


class PartnerType(models.Model):
    """
    Indicate the relationship with an entity.
    These relationship may include such as Customer, Supplier, etc.
    """
    type = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str(self):
        return self.type


class ContactInfoData(models.Model):
    """
    Indicate how to contact a person or a company.
    """

    METHODS = (
        ('tel', 'Telephone'),
        ('fax', 'Fax'),
        ('email', 'Email'),
        ('wechat', 'Wechat'),
        ('address', 'Address'),
        ('website', 'Website'),
        ('other', 'Other'),
    )

    CATEGORY = (
        ('personal', 'Personal'),
        ('office', 'Office'),
        ('home', 'Home'),
        ('other', 'Other'),
    )

    method = models.CharField(max_length=10, default='tel', choices=METHODS)
    category = models.CharField(max_length=10, default='personal', choices=CATEGORY)
    content = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str(self):
        return '{}:{}:{}'.format(self.category, self.method, self.content)


class BusinessEntity(models.Model):
    """
    The business entity is always the one we should work with. It may have its owner or employee,
    but we it's the entity we should make an operation belong to.
    """
    entity_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    objects = EntityManager()

    def __str__(self):
        return self.entity_name

    def get_name(self):
        return self.__str__()


class EntityRole(models.Model):
    """
    Indicate a relationship with a business entity, a business entity alone may be a customer or supplier.
    """
    entity = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)
    role = models.ForeignKey(PartnerType, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entity.get_name()


class EntityImage(ImageBase):
    """
    Use to save general images related to a specific business entity.
    """
    entity = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)

    def __str__(self):
        return self.entity.get_name()


class EntityContactInfo(models.Model):
    """
    Indicate how to contact with a business entity directly instead of via its employee.
    This is generally used for saving a company's address
    """
    entity = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)
    contact_info = models.ForeignKey(ContactInfoData, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entity.get_name()


class BusinessContact(models.Model):
    """
    A BusinessContact is either an employee or the entity's owner, it's a human being.
    """
    contact_name = models.CharField(max_length=100)
    entity = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}@{}'.format(self.contact_name, self.entity.get_name())


class BusinessContactInfo(models.Model):
    """
    Indicate how to contact with a person who belongs to a specific business entity.
    """
    contact = models.ForeignKey(BusinessContact, on_delete=models.CASCADE)
    contact_info = models.ForeignKey(ContactInfoData, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class BusinessContactImage(ImageBase):
    """
    It can be used to save business cards.
    """
    contact = models.ForeignKey(BusinessContact, on_delete=models.CASCADE)


class PaymentAccountType(models.Model):
    """
    How the customer paid, it may include cash, via bank, Alipay etc.
    """

    type = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)


class PaymentAccountData(models.Model):
    """
    The detailed payment account info.
    """
    owner_name = models.CharField(max_length=100)
    org_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}@{}'.format(self.owner_name, self.org_name)


class PaymentAccount(models.Model):
    """
    A complete payment account info
    """
    account_type = models.ForeignKey(PaymentAccountType, on_delete=models.CASCADE)
    account_data = models.ForeignKey(PaymentAccountData, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class EntityPayment(models.Model):
    """
    Indicate how to pay to an entity
    """
    entity = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)
    account = models.ForeignKey(PaymentAccount, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entity.get_name()

    def get_name(self):
        return self.__str__()


class EntityPaymentImage(ImageBase):
    """
    This can be used for saving bank card images if no time to provide detail data in PaymentAccount
    """
    entity_payment = models.ForeignKey(EntityPayment, on_delete=models.CASCADE)

    def __str__(self):
        return self.entity_payment.get_name()


class UnitOfCloth(models.Model):
    """
    The unit used to measure the cloth.
    """

    unit_name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unit_name

    def get_name(self):
        return self.__str__()


class CategoryOfCloth(models.Model):
    """
    Indicate the general category of cloth, such as if it's plain color,
    """
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class TextureOfCloth(models.Model):
    """
    The texture of the cloth.
    """
    texture_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.texture_name


class MaterialOfCloth(models.Model):
    """
    The material of the cloth.
    """
    material_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.material_name


class Cloth(models.Model):
    cloth_code = models.CharField(max_length=20)
    cloth_name = models.CharField(max_length=20)
    used_for = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(CategoryOfCloth, on_delete=models.SET_NULL, blank=True, null=True)
    texture = models.ForeignKey(TextureOfCloth, on_delete=models.SET_NULL, blank=True, null=True)
    material = models.ForeignKey(MaterialOfCloth, on_delete=models.SET_NULL, blank=True, null=True)
    breadth = models.IntegerField(blank=True, null=True)
    grams_per_m2 = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    added_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth_code + '_' + self.cloth_name

    def get_name(self):
        return self.__str__()


class ClothImage(ImageBase):
    """
    Show the detail of the cloth or the color card of the cloth.
    """

    IMAGE_DIR = 'images/cloth'
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)

    def __str__(self):
        return self.cloth.get_name()


class ClothInShop(models.Model):
    """
    Indicates which shop has which cloth or which cloth can be found in which shop
    It's a Many-to-Many relationship between Shop and Cloth.
    """
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    shop = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)
    shop_code = models.CharField(max_length=10, blank=True, null=True)
    num_of_colors = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_detail = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    added_time = models.DateField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.get_name() + '@' + self.shop.get_name()

    def get_name(self):
        return self.__str__()


class ClothInShopColor(models.Model):
    """
    The color of the cloth which belongs to a certain shop.
    """
    cloth_in_shop = models.ForeignKey(ClothInShop, on_delete=models.CASCADE)
    color_id = models.CharField(max_length=20)
    color_name = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth_in_shop.get_name()


class ClothInShopImage(ImageBase):
    """
    Typically used to save the color card of the cloth which is provided by a certain shop
    """
    cloth_in_shop = models.ForeignKey(ClothInShop, on_delete=models.CASCADE)

    def __str__(self):
        return self.cloth_in_shop.get_name()


class ClothColorMap(models.Model):
    """
    Used for mapping two vendor's color for the same cloth
    """
    cloth_internal = models.ForeignKey(ClothInShopColor, related_name='internal', on_delete=models.CASCADE)
    cloth_external = models.ForeignKey(ClothInShopColor, related_name='external', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth_in_shop.get_name()


class RollOfCloth(models.Model):
    """
    Describe the property of a roll of cloth, such as color, length etc.
    """

    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT)
    color_id = models.CharField(max_length=20)
    color_name = models.CharField(max_length=20)
    item_id = models.CharField(max_length=20, unique=True)
    batch_id = models.CharField(max_length=20, blank=True, null=True)
    meter = models.FloatField()
    description = models.TextField(max_length=1000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.get_name()

    def generate_item_id(self):
        """TODO"""
        self.item_id = self.color_id


class Warehouse(models.Model):
    name = models.CharField(max_length=20)
    person_in_charge = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WarehouseContactInfo(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    contact_info = models.ForeignKey(ContactInfoData, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class Inventory(models.Model):
    roll_of_cloth = models.ForeignKey(RollOfCloth, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    stock_in_date = models.DateField(auto_now_add=False)
    stock_out_date = models.DateField(auto_now_add=False, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    objects = StockManager()

    def __str__(self):
        return self.cloth.get_name()


class PieceOfCloth(models.Model):
    belong_to = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    sale_meter = models.FloatField()
    manual_adjust = models.FloatField(blank=True, null=True)
    order_date = models.DateField(auto_now_add=False)
    description = models.TextField(max_length=1000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.belong_to.cloth.get_name()


class Order(models.Model):
    serial_no = models.CharField(max_length=20)
    internal_id = models.CharField(max_length=20)
    customer = models.ForeignKey(BusinessEntity, related_name='customer', on_delete=models.PROTECT)
    supplier = models.ForeignKey(BusinessEntity, related_name='supplier', on_delete=models.PROTECT)
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT)
    color_id = models.CharField(max_length=20)
    color_name = models.CharField(max_length=20)
    price_per_unit = models.FloatField()
    total_units = models.FloatField()
    total_rolls = models.FloatField()
    total_price = models.FloatField()
    is_not_paid = models.BooleanField(default=False)
    is_withdrawn = models.BooleanField(default=False)
    is_warehouse = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    description = models.TextField(max_length=1000, blank=True, null=True)
    order_date = models.DateField(auto_now=False, auto_now_add=False, auto_created=False)
    deleted_date = models.DateField(auto_now=False, auto_now_add=False, auto_created=False)
    timestamp = models.DateTimeField(auto_now=True)

    objects = OrderManager()

    def __str__(self):
        return self.serial_no + ':' + self.customer.get_name()

    def get_name(self):
        return self.__str__()

    def generate_internal_id(self):
        """TODO"""
        self.internal_id = self.serial_no


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meter = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order.__str__()


class OrderImage(ImageBase):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.get_name()
