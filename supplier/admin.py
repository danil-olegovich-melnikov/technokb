from django.contrib import admin
from supplier.models import Suplier, SuplierOrder
# from product.models import Transaction
from product.admin import ComingTransactionInline

# Register your models here.
class SuplierAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    search_fields = ('first_name','last_name', 'telephone')
    list_display = ('telephone', 'first_name', 'last_name', 'city')
    autocomplete_fields = ['city',]
    exclude = ('profit', )  
    
    class Meta:
        model = Suplier




class ComingTransactionInline(ComingTransactionInline):
    fields = (
        'product',
        'count',
        'price',
        'order_from_supplier',
        'created_at',
    )

class SuplierOrderAdmin(admin.ModelAdmin):
    model = SuplierOrder
    inlines = [ComingTransactionInline]
    autocomplete_fields = ('suplier',) 
    list_display = ['suplier', 'created_at', 'updated_at']


admin.site.register(Suplier, SuplierAdmin)
admin.site.register(SuplierOrder,SuplierOrderAdmin)
