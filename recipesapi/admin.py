from django.contrib import admin
from .models import Item


admin.site.register(Item) #registering model with admin site, this dont really need to be here when working with MySQL, not SQLlite