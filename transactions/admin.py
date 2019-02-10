from django.contrib import admin

from .models import Transaction, TransactionDetail

admin.site.register(Transaction)
admin.site.register(TransactionDetail)

class TransactionDetailAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity']
    #readonly_fields = ('price_discounted_calculated', 'discount_calculated', 'price_regular_calculated', 'price_final', 'price_extended')
