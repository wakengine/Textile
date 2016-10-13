from django.db import models

from common.form_data import FormData
from stock.models import Company, Cloth


class OrderManager(models.Manager):
    def get_total_price(self):
        total_price = 0
        all_list = self.all()
        for item in all_list:
            total_price += item.total_price
        return total_price


class Order(models.Model):
    serial_no = models.CharField(max_length=20, verbose_name='单号', help_text='(所在单号)')
    internal_id = models.CharField(max_length=20, verbose_name='订单编号')
    customer = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='顾客')
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT, verbose_name='布料')
    color = models.CharField(max_length=20, verbose_name='颜色')
    price_per_unit = models.FloatField(verbose_name='单价')
    total_units = models.FloatField(verbose_name='总米数/重量', help_text='(单位为m或kg)')
    total_bundles = models.FloatField(default=0, blank=True, verbose_name='总匹数')
    total_price = models.FloatField(verbose_name='总价')
    is_not_paid = models.BooleanField(default=False, verbose_name='欠款')
    is_withdrawn = models.BooleanField(default=False, verbose_name='退单')
    is_warehouse = models.BooleanField(default=False, verbose_name='仓库')
    description = models.TextField(max_length=1000, blank=True, verbose_name='详细描述')
    order_date = models.DateField(auto_now=False, auto_now_add=False, auto_created=False, verbose_name='下单日期')
    timestamp = models.DateTimeField(auto_now=True)

    objects = OrderManager()

    @staticmethod
    def get_form_data():
        customer_list = Company.objects.all()
        customers = []
        for customer in customer_list:
            customers.append('{}__{}'.format(customer.get_name(), customer.pk))

        cloth_list = Cloth.objects.all()
        clothes = []
        for cloth in cloth_list:
            clothes.append('{}__{}'.format(cloth.get_name(), cloth.pk))

        form_list = [FormData('单号', 'serial_no', True, 'text', 20, '单号', None),
                     FormData('客户', 'customer', True, 'datalist', 0, '', customers),
                     FormData('布料', 'cloth', True, 'datalist', 0, '', clothes),
                     FormData('颜色', 'color', True, 'text', 20, '色号', None),
                     FormData('单价', 'price_per_unit', True, 'number', 1000, '0.0', None),
                     FormData('总米数/重量', 'total_units', True, 'number', 100000, '0.0', None),
                     FormData('总匹数', 'total_bundles', True, 'number', 1000, '0.0', None),
                     FormData('下单日期', 'order_date', True, 'date', 0, '', None),
                     FormData('欠款', 'is_not_paid', False, 'checkbox', 0, '', None),
                     FormData('退单', 'is_withdrawn', False, 'checkbox', 0, '', None),
                     FormData('仓库', 'is_warehouse', False, 'checkbox', 0, '', None),
                     FormData('详细描述', 'description', False, 'textarea', 1000, '添加详细描述', None),
                     ]

        return form_list

    def __str__(self):
        return self.serial_no + ':' + self.customer.get_name()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='所属订单')
    meter = models.FloatField(verbose_name='米数')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order.__str__()


class OrderImage(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    img_path = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order.__str__()
