from django.db import models

from .models import *


class EntityManager(models.Manager):
    """
    Manage BusinessEntity related models.
    """

    @staticmethod
    def create_entity_from_form_data(form):
        """
        Create an instance of Entity from form data
        :param form: Form data posted by user
        :return: An instance of Entity
        """
        entity = BusinessEntity()
        entity.entity_name = form['entity_name']
        return entity


class ClothManager(models.Manager):
    @staticmethod
    def create_cloth_from_form_data(form):
        """Create an instance of Cloth from form data
        :param form: Form data posted by user
        :return: An instance of Cloth
        """
        cloth = Cloth()
        cloth.cloth_code = form['serial_no']
        return cloth


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
