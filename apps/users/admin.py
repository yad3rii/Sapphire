from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "nickname",
        "balance",
        "is_seller",
        "rating",
        "successful_deals",
        "created_at",
    )
    list_filter = ("is_seller", "created_at")
    search_fields = ("user__username", "user__email", "nickname")