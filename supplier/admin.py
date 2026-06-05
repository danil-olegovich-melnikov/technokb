from django.contrib import admin
from supplier.models import Suplier, SuplierOrder
from product.models import Transaction


# Register your models here.
class SuplierAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'profit',)
    search_fields = ('first_name','last_name', 'telephone')
    list_display = ('telephone', 'first_name', 'last_name', 'profit', 'city')
    autocomplete_fields = ['city',]
    
    class Meta:
        model = Suplier




class ComingTransactionInline(admin.TabularInline):
    model = Transaction
    autocomplete_fields = ('product',)
    exclude = ('order',)
    extra =  1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(action=Transaction.COMING)

class SuplierOrderAdmin(admin.ModelAdmin):
    model = SuplierOrder
    inlines = [ComingTransactionInline]
    autocomplete_fields = ('suplier',) 
    list_display = ['suplier', 'created_at', 'updated_at']


admin.site.register(Suplier, SuplierAdmin)
admin.site.register(SuplierOrder,SuplierOrderAdmin)
