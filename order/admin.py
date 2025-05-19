from django.contrib import admin
from .models import Order

from django.utils.html import format_html

from product.models import Transaction
# Register your models here.

class TransactionAdmin(admin.TabularInline):
    model = Transaction     

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [TransactionAdmin]
    readonly_fields = ("telephone", "whatsapp",)
    fields = ("client", "image", "telephone", "whatsapp", )

    def whatsapp(self,obj):
        url = f"https://wa.me/+996{obj.client.telephone}"
        return format_html('<a href="{}" terget="_blank">{}</a>', url,url)
    
    def telephone(self,obj):
        return (f"Номер: {obj.client.telephone}")



admin.site.register(Order,OrderAdmin)



