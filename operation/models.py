from django.db import models

from base.models import BusinessEntity, Cloth, Image


class StockManager(models.Manager):
    @staticmethod
    def create_inventory_from_form_data(form):
        """Create an instance of Inventory from form data
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


class RollOfCloth(models.Model):
    """
    Describe the property of a roll of cloth, such as color, length etc.
    """

    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT)
    color_id = models.CharField(max_length=20)
    color_name = models.CharField(max_length=20, blank=True)
    item_id = models.CharField(max_length=20, unique=True)
    batch_id = models.CharField(max_length=20, blank=True)
    meter = models.FloatField()
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.get_name()

    def generate_item_id(self):
        """TODO"""
        self.item_id = self.color_id


class Warehouse(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=20, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    roll_of_cloth = models.ForeignKey(RollOfCloth, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    stock_in_date = models.DateField(auto_now_add=False)
    stock_out_date = models.DateField(auto_now_add=False, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    objects = StockManager()

    def __str__(self):
        return self.cloth.get_name()


class PieceOfCloth(models.Model):
    belong_to = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    sale_meter = models.FloatField()
    manual_adjust = models.FloatField(default=0.0, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    order_date = models.DateField(auto_now_add=False)
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
    description = models.TextField(max_length=1000, blank=True)
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


class OrderImage(Image):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.get_name()
