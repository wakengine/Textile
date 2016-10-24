from django.db import models

from asset.models import Cloth


class StockManager(models.Manager):
    pass


class WholeSale(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT)
    color = models.CharField(max_length=20)
    batch_id = models.CharField(max_length=20)
    is_in_stock = models.BooleanField(default=True)
    put_in_time = models.DateField(auto_now_add=False)
    sale_time = models.DateField(auto_now_add=False, blank=True)
    meter = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    objects = StockManager()

    def __str__(self):
        return self.cloth.get_name()


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
