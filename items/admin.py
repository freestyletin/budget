from django.contrib import admin

from .models import GenericItem, Item

admin.site.register(GenericItem)
admin.site.register(Item)
