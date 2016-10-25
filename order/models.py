from django.db import models

from asset.models import Entity, Cloth, Image


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


class Order(models.Model):
    serial_no = models.CharField(max_length=20)
    internal_id = models.CharField(max_length=20)
    customer = models.ForeignKey(Entity, on_delete=models.PROTECT)
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT)
    color = models.CharField(max_length=20)
    price_per_unit = models.FloatField()
    total_units = models.FloatField()
    total_rolls = models.FloatField(default=0, blank=True)
    total_price = models.FloatField()
    is_not_paid = models.BooleanField(default=False)
    is_withdrawn = models.BooleanField(default=False)
    is_warehouse = models.BooleanField(default=False)
    description = models.TextField(max_length=1000, blank=True)
    order_date = models.DateField(auto_now=False, auto_now_add=False, auto_created=False)
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
