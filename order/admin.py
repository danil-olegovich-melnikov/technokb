from django.contrib import admin
from .models import Order

from product.models import Transaction
# Register your models here.

class TransactionAdmin(admin.TabularInline):
    model = Transaction     

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [TransactionAdmin]



admin.site.register(Order,OrderAdmin)



