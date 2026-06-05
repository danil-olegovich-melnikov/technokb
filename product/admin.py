from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from urllib.parse import urlencode

from product.models import Category, Product, Transaction, ProductPhoto
from django.forms.models import BaseInlineFormSet



# =========================
# BASE TRANSACTION INLINE
# =========================



class BaseTransactionInlineFormSet(BaseInlineFormSet):
    ACTION = None  # будет прокинут динамически

    def save_new_objects(self, commit=True):
        objects = super().save_new_objects(commit=commit)

        for obj in objects:
            print("Создан новый inline объект:", obj)

            if self.ACTION:
                obj.action = self.ACTION
                obj.save()

        return objects
    

class BaseTransactionInline(admin.TabularInline):
    model = Transaction
    extra = 1
    readonly_fields = ('created_at',)

    ACTION = None

    formset = BaseTransactionInlineFormSet

    def get_queryset(self, request):
        return super().get_queryset(request).filter(action=self.ACTION)

    def get_formset(self, request, obj=None, **kwargs):
        FormSet = super().get_formset(request, obj, **kwargs)

        # 🔥 прокидываем ACTION в formset класс
        FormSet.ACTION = self.ACTION

        return FormSet

class ComingTransactionInline(BaseTransactionInline):
    ACTION = Transaction.COMING

    verbose_name = "Приход"
    verbose_name_plural = "Приходы"

    fields = (
        'count',
        'price',
        'order_from_supplier',
        'created_at',
    )


class LeavingTransactionInline(BaseTransactionInline):
    ACTION = Transaction.LEAVING

    verbose_name = "Уход"
    verbose_name_plural = "Уходы"

    fields = (
        'count',
        'price',
        'order',
        'created_at',

    )


class TransferTransactionInline(BaseTransactionInline):
    ACTION = Transaction.TRANSFER

    verbose_name = "Переход"
    verbose_name_plural = "Переходы"

    fields = (
        'count',
        'price',
        'created_at',
    )


# =========================
# PRODUCT PHOTO INLINE
# =========================
class AdminPhoto(admin.TabularInline):
    model = ProductPhoto
    extra = 1


# =========================
# CATEGORY ADMIN
# =========================
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)


# =========================
# FILTER
# =========================
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
        return [c for c in choices if c['display'] != _('All')]

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(in_stock="Да")
        if self.value() == 'no':
            return queryset.filter(in_stock="Нет")
        return queryset


# =========================
# PRODUCT ADMIN
# =========================
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        AdminPhoto,
        ComingTransactionInline,
        LeavingTransactionInline,
        TransferTransactionInline,
    ]

    list_display = (
        'name',
        'category',
        'count',
        'average_price',
        'in_stock',
        'is_published',
        'created_at',
        'amount_of_transaction',
    )

    search_fields = ('name', 'category__name')
    list_filter = ('category', InStockFilter, 'is_published')
    ordering = ('name',)

    readonly_fields = (
        'count',
        'average_price',
        'total_count',
        'in_stock',
        'created_at',
        'amount_of_transaction',
    )

    autocomplete_fields = ('category',)
    list_editable = ['is_published']

    def changelist_view(self, request, extra_context=None):
        if 'in_stock' not in request.GET:
            query_string = urlencode({'in_stock': 'yes'})
            return redirect(f"{request.path}?{query_string}")
        return super().changelist_view(request, extra_context)


# =========================
# REGISTER
# =========================
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)