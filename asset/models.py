from django.db import models


class Image(models.Model):
    """
    Base image class, may be used by any model.
    """

    image = models.FileField()
    path = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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


class PartnerType(models.Model):
    """
    Indicate the relationship with an entity.
    These relationship may include such as Customer, Supplier, etc.
    """
    type = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    def __str(self):
        return self.type


class ContactWayData(models.Model):
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
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str(self):
        return '{}:{}:{}'.format(self.category, self.method, self.content)


class BusinessEntity(models.Model):
    """
    The business entity is always the one we should work with. It may have its owner or employee,
    but we it's the entity we should make an order belong to.
    """
    entity_name = models.CharField(max_length=20)
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    objects = EntityManager()

    def __str__(self):
        return self.entity_name

    def get_name(self):
        return self.__str__()


class EntityRoleMap(models.Model):
    """
    Indicate a relationship with a business entity, a business entity alone may be a customer or supplier.
    """
    entity = models.ForeignKey(BusinessEntity, on_delete=models.PROTECT)
    role = models.ForeignKey(PartnerType, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entity.get_name()


class EntityImage(Image):
    """
    Use to save general images related to a specific business entity.
    """
    entity = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)

    def __str__(self):
        return self.entity.get_name()


class EntityContactWay(models.Model):
    """
    Indicate how to contact with a business entity directly instead of via its employee.
    This is generally used for saving a company's address
    """
    entity = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)
    contact_way = models.ForeignKey(ContactWayData, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entity.get_name()


class BusinessContact(models.Model):
    """
    A BusinessContact is either an employee or the entity's owner, it's a human being.
    """
    contact_name = models.CharField(max_length=10, blank=True)
    entity = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)
    position = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}@{}'.format(self.contact_name, self.entity.get_name())


class BusinessContactWay(models.Model):
    """
    Indicate how to contact with a person who belongs to a specific business entity.
    """
    contact = models.ForeignKey(BusinessContact, on_delete=models.CASCADE)
    contact_way = models.ForeignKey(ContactWayData, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class BusinessContactImage(Image):
    """
    It can be used to save business cards.
    """
    contact = models.ForeignKey(BusinessContact, on_delete=models.CASCADE)


class PaymentAccountType(models.Model):
    """
    How the customer paid, it may include cash, via bank, Alipay etc.
    """

    type = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)


class PaymentAccountData(models.Model):
    owner_name = models.CharField(max_length=20)
    org_name = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}@{}'.format(self.owner_name, self.org_name)


class PaymentAccount(models.Model):
    account_type = models.ForeignKey(PaymentAccountType, on_delete=models.PROTECT)
    account_data = models.ForeignKey(PaymentAccountData, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now=True)


class EntityPayment(models.Model):
    entity = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)
    account = models.ForeignKey(PaymentAccount, on_delete=models.PROTECT)
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entity.get_name()

    def get_name(self):
        return self.__str__()


class EntityPaymentImage(Image):
    """
    This can be used for saving bank card images if no time to provide detail data in PaymentAccount
    """
    entity_payment = models.ForeignKey(EntityPayment, on_delete=models.CASCADE)

    def __str__(self):
        return self.entity_payment.get_name()


class ClothManager(models.Manager):
    @staticmethod
    def create_cloth_from_form_data(form):
        """Create an instance of Cloth from form data
        :param form: Form data posted by user
        :return: An instance of Cloth
        """
        cloth = Cloth()
        cloth.serial_no = form['serial_no']
        return cloth


class Cloth(models.Model):
    serial_no = models.CharField(max_length=20)
    cloth_name = models.CharField(max_length=20, blank=True)
    width = models.IntegerField(default=150, blank=True)
    used_for = models.CharField(max_length=100, blank=True)
    grams_per_m2 = models.FloatField(blank=True)
    description = models.TextField(max_length=1000, blank=True)
    added_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serial_no + '_' + self.cloth_name

    def get_name(self):
        return self.__str__()


class ClothImage(Image):
    """
    Show the detail of the cloth or the color card of the cloth.
    """
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)

    def __str__(self):
        return self.cloth.get_name()


class ClothCategory(models.Model):
    """
    Indicate the general category of cloth, such as if it's plain color,
    """
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class CategoryOfCloth(models.Model):
    """
    Indicate what category the cloth belongs to.
    """
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    category = models.ForeignKey(ClothCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)


class ClothTexture(models.Model):
    """
    The texture of the cloth.
    """
    texture_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.texture_name


class TextureOfCloth(models.Model):
    """
    Indicate what texture the cloth is formed.
    """
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    category = models.ForeignKey(ClothTexture, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)


class ClothMaterial(models.Model):
    """
    The material of the cloth.
    """
    material_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.material_name


class MaterialOfCloth(models.Model):
    """
    Indicate what material the cloth is made by.
    """
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    category = models.ForeignKey(ClothMaterial, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)


class ClothUnit(models.Model):
    """
    The unit used to measure the cloth.
    """

    SALE_UNIT = (
        ('M', 'Meter'),
        ('Y', 'Yard'),
        ('KG', 'Kilogram'),
    )

    unit_name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unit_name

    def get_name(self):
        return self.__str__()


class ClothUnitConversion(models.Model):
    """
    How one unit converted to another unit.
    """
    unit_from = models.ForeignKey(ClothUnit, on_delete=models.CASCADE)
    unit_to = models.ForeignKey(ClothUnit, on_delete=models.CASCADE)
    formula = models.FloatField()
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}->{}'.format(self.unit_from.unit_name, self.unit_to.unit_name)


class ClothInShop(models.Model):
    """
    Indicates which shop has which cloth or which cloth can be found in which shop
    It's a Many-to-Many relationship between Shop and Cloth.
    """
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    shop = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)
    shop_code = models.CharField(max_length=10, blank=True)
    num_of_colors = models.IntegerField(default=0, blank=True)
    price = models.FloatField(default=0, blank=True)
    price_detail = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True)
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
    cloth = models.ForeignKey(ClothInShop, on_delete=models.CASCADE)
    color_id = models.CharField(max_length=20)
    color_name = models.CharField(max_length=20, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.get_name()


class ClothInShopImage(Image):
    """
    Mainly used to save the color card of the cloth which provided by a certain shop
    """
    cloth_in_shop = models.ForeignKey(ClothInShop, on_delete=models.CASCADE)

    def __str__(self):
        return self.cloth_in_shop.get_name()


class ColorMap(models.Model):
    """
    Used for mapping two vendor's color for the same cloth
    """
    cloth_internal = models.ForeignKey(ClothInShop, on_delete=models.CASCADE)
    cloth_external = models.ForeignKey(ClothInShop, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth_in_shop.get_name()
