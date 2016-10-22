from django.db import models

from asset.models import Cloth


class StockManager(models.Manager):
    def list_for_cloth(self, cloth, color):
        return self.all().count()


class WholeSale(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT, verbose_name='布料')
    color = models.CharField(max_length=20, verbose_name='颜色')
    batch_id = models.CharField(max_length=20, verbose_name='缸号')
    is_in_stock = models.BooleanField(default=True)
    put_in_time = models.DateField(auto_now_add=False, verbose_name='入库时间')
    sale_time = models.DateField(auto_now_add=False, blank=True, verbose_name='出库时间')
    meter = models.FloatField(verbose_name='米数')
    timestamp = models.DateTimeField(auto_now=True)

    objects = StockManager()

    def __str__(self):
        return self.cloth.get_name()


class Retail(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT, verbose_name='布料')
    color = models.CharField(max_length=20, verbose_name='颜色')
    remain_meter = models.FloatField(verbose_name='剩余米数')
    wastage_meter = models.FloatField(verbose_name='损耗米数')
    put_in_time = models.DateField(auto_now_add=False, verbose_name='入库时间')
    sale_time = models.DateField(auto_now_add=False, blank=True, verbose_name='出库时间')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''
