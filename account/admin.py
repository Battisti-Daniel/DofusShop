from django.contrib import admin
from .models import Account, Item, Gear, Server


def addAdm(*kwargs):
    for model in kwargs:
        admin.site.register(model)


addAdm(Account, Item, Gear, Server)
