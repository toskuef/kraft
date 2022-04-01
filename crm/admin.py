from django.contrib import admin
from .models import *


admin.site.register(Customer)
admin.site.register(SourceCustomer)
admin.site.register(Address)
admin.site.register(AddressCountry)
admin.site.register(AddressArea)
admin.site.register(AddressRegion)
admin.site.register(AddressTown)
admin.site.register(AddressStreet)
admin.site.register(Order)
admin.site.register(TypePay)
