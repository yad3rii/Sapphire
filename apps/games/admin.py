from django.contrib import admin

from .models import Category, Game


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1
    prepopulated_fields = {
        "slug": ("title",),
    }


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "is_popular",
        "created_at",
    )
    list_filter = ("is_popular", "created_at")
    search_fields = ("title", "description")
    prepopulated_fields = {
        "slug": ("title",),
    }
    inlines = [CategoryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "game",
        "slug",
    )
    list_filter = ("game",)
    search_fields = ("title", "game__title", "description")
    prepopulated_fields = {
        "slug": ("title",),
    }