from django.contrib import admin
from .models import Wallet, Address, Information

# Register your models here.

admin.site.register(Wallet)
admin.site.register(Address)
admin.site.register(Information)
