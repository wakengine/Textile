from django.db import models

from stock.models import Shop, Cloth


class OrderManager(models.Manager):
    def get_total_price(self):
        total_price = 0
        all_list = self.all()
        for item in all_list:
            total_price += item.total_price
        return total_price


class Order(models.Model):
    serial_no = models.CharField(max_length=20, verbose_name='单号', help_text='(所在单号)')
    customer = models.ForeignKey(Shop, on_delete=models.PROTECT, verbose_name='顾客')
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT, verbose_name='布料')
    color = models.CharField(max_length=20, verbose_name='颜色')
    price_per_unit = models.FloatField(verbose_name='单价')
    total_units = models.FloatField(verbose_name='总米数/克重', help_text='(单位为m或kg)')
    total_bundles = models.FloatField(default=0, blank=True, verbose_name='总匹数')
    total_price = models.FloatField(verbose_name='总价')
    total_paid = models.FloatField(default=0, blank=True, verbose_name='已付金额')
    is_withdrawn = models.BooleanField(default=False, verbose_name='是否为退单')
    is_warehouse = models.BooleanField(default=False, verbose_name='是否为仓库')
    order_date = models.DateField(auto_now=False, auto_now_add=False, auto_created=False, verbose_name='下单日期')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serial_no + ':' + self.customer.get_name()

    objects = OrderManager()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='所属订单')
    meter = models.FloatField(verbose_name='米数')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.belong_to.__str__()


class OrderImage(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    img_path = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
