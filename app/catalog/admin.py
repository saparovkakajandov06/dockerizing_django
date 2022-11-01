from django.contrib import admin
from .models import Characteristic, Product, Filial, FilialPrice

# Register your models here.

admin.site.register(Characteristic)
admin.site.register(Product)
admin.site.register(Filial)
admin.site.register(FilialPrice)
