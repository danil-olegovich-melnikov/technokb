from django.contrib import admin
from product.models import Category,Product,Transaction,ProductPhoto
from django.utils.translation import gettext_lazy as _
from mptt.admin import MPTTModelAdmin,TreeRelatedFieldListFilter
from django.shortcuts import redirect
from urllib.parse import urlencode

# Register your models here.

admin.site.site_header = 'Администрация TechnoKB'
admin.site.index_title = 'Наши модели'
admin.site.site_title = 'Продукты - Административная панель'

class TransactionAdmin(admin.TabularInline):
    model = Transaction
    list_display = ('created_at',)
    readonly_fields = ('created_at',)  
    extra = 1  

class AdminPhoto(admin.TabularInline):
    model = ProductPhoto
    extra = 1


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name','parent')
    list_filter = (('parent', admin.RelatedFieldListFilter),)
    search_fields = ('name',)

class InStockFilter(admin.SimpleListFilter):
    title = _('В наличии')  
    parameter_name = 'in_stock'

    def lookups(self, request, model_admin):
        return [
            ('yes', _('Да')),
            ('no', _('Нет')),
        ]
    
    def choices(self, changelist):
        choices = super().choices(changelist)
        return [choice for choice in choices if choice['display'] != _('All')]

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(in_stock="Да")
        if self.value() == 'no':
            return queryset.filter(in_stock="Нет")
        return queryset


class ProductAdmin(admin.ModelAdmin):
    
    inlines = [AdminPhoto,TransactionAdmin]    
    list_display = ('name','category','count','in_stock','is_published','created_at','amount_of_transaction',)
    search_fields = ('name',)
    list_filter = (('category',TreeRelatedFieldListFilter),InStockFilter,)   
    ordering = ('name',)
    readonly_fields = ('count','average_price','total_count','in_stock','created_at','amount_of_transaction',)
    autocomplete_fields = ('category',) 

    class Meta:
        model = Product
       
    def changelist_view(self, request, extra_context=None):        
        if 'in_stock' not in request.GET:
            query_string = urlencode({'in_stock': 'yes'})
            return redirect(f"{request.path}?{query_string}")
        return super().changelist_view(request, extra_context)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)


