from django.db import models

from asset.models import Company, Cloth


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
