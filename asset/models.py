from django.db import models


class Image(models.Model):
    """Base image class"""
    image = models.FileField()
    description = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EntityManager(models.Manager):
    @staticmethod
    def create_entity_from_form_data(form):
        """Create an instance of Entity from form data
        :param form: Form data posted by user
        :return: An instance of Entity
        """
        entity = Entity()
        entity.entity_name = form['entity_name']
        entity.relationship = form['relationship']
        entity.description = form['description']
        return entity


class Entity(models.Model):
    RelationShip = (
        ('C', 'Customer'),
        ('S', 'Supplier'),
        ('B', 'Both'),
    )

    entity_name = models.CharField(max_length=20)
    relationship = models.CharField(max_length=1, default='C', choices=RelationShip)
    telephone = models.CharField(max_length=20, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    objects = EntityManager()

    def __str__(self):
        return self.entity_name

    def save(self, *args, **kwargs):
        super(Entity, self).save(*args, **kwargs)

    def get_name(self):
        return self.__str__()


class BankInfo(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=20)
    bank_number = models.CharField(max_length=20)
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entity.get_name()


class EntityContact(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=10, blank=True)
    position = models.CharField(max_length=10, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entity.get_name()


class EntityImage(Image):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return self.entity.get_name()


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
    shop = models.ForeignKey(Entity, on_delete=models.CASCADE)
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
