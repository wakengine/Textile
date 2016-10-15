from django.db import models

from stock.models import Company, Cloth
from utils.form_utils import FormData, FormReader


class OrderManager(models.Manager):
    ID_PREFIX = '__'

    @staticmethod
    def get_form_data():
        customer_list = Company.objects.all()
        customers = []
        for customer in customer_list:
            customers.append('{}{}{}'.format(customer.get_name(), OrderManager.ID_PREFIX, customer.pk))

        cloth_list = Cloth.objects.all()
        clothes = []
        for cloth in cloth_list:
            clothes.append('{}{}{}'.format(cloth.get_name(), OrderManager.ID_PREFIX, cloth.pk))

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
                     FormData('上传图片', 'image', False, 'file', 0, '', None),
                     FormData('详细描述', 'description', False, 'textarea', 1000, '添加详细描述', None),
                     ]

        return form_list

    @staticmethod
    def read_and_save_order(request):
        form = FormReader(request)

        serial_no = form.get_post_data('serial_no')
        customer = form.get_post_data('customer')
        cloth = form.get_post_data('cloth')
        color = form.get_post_data('color')
        price_per_unit = float(form.get_post_data('price_per_unit'))
        total_units = float(form.get_post_data('total_units'))
        total_bundles = float(form.get_post_data('total_bundles'))
        order_date = form.get_post_data('order_date')
        is_not_paid = form.get_post_data('is_not_paid')
        is_withdrawn = form.get_post_data('is_withdrawn')
        is_warehouse = form.get_post_data('is_warehouse')
        description = form.get_post_data('description')

        _, _, customer_id = customer.partition(OrderManager.ID_PREFIX)
        if not customer_id:
            new_customer = Company()
            new_customer.name = customer
            new_customer.owner_name = customer
            new_customer.relationship = 'C'
            new_customer.save()
            customer_id = new_customer.pk

        _, _, cloth_id = cloth.partition(OrderManager.ID_PREFIX)
        if not cloth_id:
            new_cloth = Cloth()
            new_cloth.serial_no = cloth
            new_cloth.name = cloth
            new_cloth.save()
            cloth_id = new_cloth.pk

        order = Order()

        order.serial_no = serial_no
        order.internal_id = serial_no  # WA for now
        order.customer_id = customer_id
        order.cloth_id = cloth_id
        order.color = color
        order.price_per_unit = price_per_unit
        order.total_units = total_units
        order.total_price = price_per_unit * total_units
        order.total_bundles = total_bundles
        order.order_date = order_date
        order.is_not_paid = True if is_not_paid else False
        order.is_withdrawn = True if is_withdrawn else False
        order.is_warehouse = True if is_warehouse else False
        order.description = description

        order.save()
        return order

    def get_total_price(self):
        total_price = 0.0
        all_list = self.all()
        for item in all_list:
            total_price += item.total_price

        return format(total_price, ',')


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
