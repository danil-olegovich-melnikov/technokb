from django.contrib import admin
from .models import Category, Equipment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "buy_price",
        "sell_price",
        "created_at",
    )
    autocomplete_fields = ['category', ]
    list_filter = (
        "category",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = ("-created_at",)

    readonly_fields = ("created_at",)

    fieldsets = (
        ("Основная информация", {
            "fields": (
                "name",
                "description",
                "category",
            )
        }),

        ("Цены", {
            "fields": (
                "buy_price",
                "sell_price",
            )
        }),

        ("Система", {
            "fields": (
                "created_at",
            )
        }),
    )