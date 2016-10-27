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


class ContactType(models.Model):
    """
    Indicate the relationship with an entity.
    These relationship may include such as Customer, Supplier, etc.
    """
    type = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    def __str(self):
        return self.type


class ContactData(models.Model):
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
    entity_name = models.CharField(max_length=20)
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    objects = EntityManager()

    def __str__(self):
        return self.entity_name

    def get_name(self):
        return self.__str__()


class EntityRoleMap(models.Model):
    entity = models.ForeignKey(BusinessEntity, on_delete=models.PROTECT)
    role = models.ForeignKey(ContactType, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entity.get_name()


class EntityImage(Image):
    entity = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)

    def __str__(self):
        return self.entity.get_name()


class BusinessContact(models.Model):
    contact_name = models.CharField(max_length=10, blank=True)
    entity = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)
    position = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}@{}'.format(self.contact_name, self.entity.get_name())


class EntityContactImage(Image):
    contact = models.ForeignKey(BusinessContact, on_delete=models.CASCADE)


class BusinessContactDetail(models.Model):
    contact = models.ForeignKey(BusinessContact, on_delete=models.CASCADE)
    method = models.ForeignKey(ContactData, on_delete=models.CASCADE)


class PaymentAccountType(models.Model):
    """
    How the customer paid, it may include cash, via bank, alipay etc.
    """

    type = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)


class PaymentAccountData(models.Model):
    user_name = models.CharField(max_length=20)
    org_name = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)


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
    SALE_UNIT = (
        ('M', 'Meter'),
        ('Y', 'Yard'),
        ('KG', 'Kilogram'),
    )
    serial_no = models.CharField(max_length=20)
    cloth_name = models.CharField(max_length=20, blank=True)
    material = models.CharField(max_length=20, blank=True)
    texture = models.CharField(max_length=20, blank=True)
    width = models.IntegerField(default=150, blank=True)
    ref_price = models.FloatField(default=0, blank=True)
    is_per_meter = models.BooleanField(default=True)
    used_for = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serial_no + '_' + self.cloth_name

    def get_name(self):
        return self.__str__()


class ColorOfCloth(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    color_id = models.CharField(max_length=10)
    color_name = models.CharField(max_length=10, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.get_name()


class ClothImage(Image):
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)

    def __str__(self):
        return self.cloth.get_name()


class ClothInShop(models.Model):
    """Indicates which shop has which cloth or which cloth can be found in which shop
    It's a Many-to-Many relationship between Shop and Cloth.
    """
    serial_no = models.CharField(max_length=10, blank=True,
                                 help_text='(Different shops which owns the same cloth have different number)')
    shop = models.ForeignKey(BusinessEntity, on_delete=models.CASCADE)
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    num_of_colors = models.IntegerField(default=0, blank=True)
    price = models.FloatField(default=0, blank=True)
    price_detail = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    created_time = models.DateField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.get_name() + '@' + self.shop.get_name()

    def get_name(self):
        return self.__str__()


class ClothInShopImage(Image):
    cloth_in_shop = models.ForeignKey(ClothInShop, on_delete=models.CASCADE)

    def __str__(self):
        return self.cloth_in_shop.get_name()


class ColorMap(models.Model):
    """Used for mapping two vendor's color for the same cloth
    """
    cloth_in_shop = models.ForeignKey(ClothInShop, on_delete=models.CASCADE)
    internal_color_id = models.CharField(max_length=10)
    internal_color_name = models.CharField(max_length=10)
    external_color_id = models.CharField(max_length=10)
    external_color_name = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth_in_shop.get_name()
