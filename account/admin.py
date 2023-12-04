from django.contrib import admin
from .models import Account, Item, Gear, Server, Transacao, Conjunto


admin.site.register([Account, Item, Gear, Server,Transacao, Conjunto])
