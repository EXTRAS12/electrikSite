from django.contrib import admin

from .models import Category, PriceCategory, WorkList


class PriceCategoryAdmin(admin.ModelAdmin):
    """Добавление товаров с ценами"""
    list_display = ('id', 'name', 'price', 'category')
    list_display_links = ('id', 'name', 'price', 'category')
    search_fields = ('name',)


class WorkListAdmin(admin.ModelAdmin):
    """Добавление фото наших работ"""
    list_display = ('id', 'title', 'created_at', 'updated_at', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(PriceCategory, PriceCategoryAdmin)
admin.site.register(WorkList, WorkListAdmin)
admin.site.register(Category, CategoryAdmin)
