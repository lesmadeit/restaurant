from django.contrib import admin
from .models import MenuCategory, MenuItem, Special


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


@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    ordering = ['order']
    prepopulated_fields = {'slug': ('title',)}
