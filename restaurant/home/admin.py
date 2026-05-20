from django.contrib import admin
from .models import MenuCategory, MenuItem


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepropulated_fields = {'slug': ('name',)}


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'description']
    ordering = ['category', 'name']
