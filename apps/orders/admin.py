from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "buyer",
        "seller",
        "listing",
        "price",
        "quantity",
        "status",
        "created_at",
    )
    list_filter = (
        "status",
        "created_at",
        "seller",
    )
    search_fields = (
        "buyer__username",
        "seller__username",
        "listing__title",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )