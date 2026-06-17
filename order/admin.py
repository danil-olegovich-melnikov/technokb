from django.contrib import admin
from .models import Order

from product.models import Transaction
# Register your models here.

class TransactionAdmin(admin.TabularInline):
    model = Transaction   
    autocomplete_fields = ('product',) 
    exclude = ('order_from_supplier', )


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [TransactionAdmin]
    autocomplete_fields = ('client',) 
    list_display = ['client', 'created_at', 'updated_at']


admin.site.register(Order,OrderAdmin)



