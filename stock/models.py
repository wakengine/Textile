from django.db import models

from asset.models import Cloth


class StockManager(models.Manager):
    @staticmethod
    def create_inventory_from_form_data(form):
        """Create an instance of Inventory from form data
        :param form: Form data posted by user
        :return: An instance of Inventory
        """
        inventory = Inventory()
        inventory.cloth = Cloth()
        return inventory


class Inventory(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT)
    color_id = models.CharField(max_length=20)
    color_name = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=True)

    objects = StockManager()

    def __str__(self):
        return self.cloth.get_name()


class StockDetail(models.Model):
    stock = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    batch_id = models.CharField(max_length=20)
    meter = models.FloatField()
    is_in_stock = models.BooleanField(default=True)
    put_in_time = models.DateField(auto_now_add=False)
    sale_time = models.DateField(auto_now_add=False, blank=True)


class Retail(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT)
    color = models.CharField(max_length=20)
    remain_meter = models.FloatField()
    wastage_meter = models.FloatField()
    put_in_time = models.DateField(auto_now_add=False)
    sale_time = models.DateField(auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.get_name()
