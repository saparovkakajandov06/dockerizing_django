from email.policy import default
from django.db import models
import os


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")

    def get_price(self):
        filial_price = FilialPrice.objects.filter(product=self).first()
        if not filial_price:
            return None
        else:
            return filial_price.price

    def __str__(self):
        return self.name


class Filial(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    region = models.IntegerField(null=True, blank=True, verbose_name="Region")

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="self_characteristics", verbose_name="Parent")
    name = models.CharField(max_length=255, verbose_name="Name")
    product = models.ManyToManyField(Product, related_name="characteristics", verbose_name="Products")

    def __str__(self):
        return self.name


class FilialPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product", related_name="filial_prices")
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, verbose_name="Filial", related_name="product_prices")
    price = models.IntegerField(default=0, verbose_name="Price")

    def get_characteristics(self):
        return self.product.characteristics.all()

    def __str__(self):
        return str(self.product.name) + " - " + str(self.filial.name) + " - " + str(self.price)
