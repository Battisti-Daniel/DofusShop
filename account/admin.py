from django.contrib import admin
from .models import Account, Item, Characteristic, Server, TypeCharacteristic


def addAdm(*kwargs):
    for model in kwargs:
        admin.site.register(model)


addAdm(Account, Item, Characteristic, Server, TypeCharacteristic)
