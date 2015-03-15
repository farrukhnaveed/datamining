from django.contrib import admin
from store.inventory.models import Category, SubCategory, Brand, Item


class CategoryAdmin(admin.ModelAdmin):
    list_display =('name', 'slug')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display =('name', 'category', 'slug')


class BrandAdmin(admin.ModelAdmin):
    list_display =('name', 'slug')


class ItemAdmin(admin.ModelAdmin):
    list_display =('name', 'sub_category', 'price', 'slug', 'status')


admin.site.register( Category, CategoryAdmin )
admin.site.register( SubCategory, SubCategoryAdmin )
admin.site.register( Brand, BrandAdmin )
admin.site.register( Item, ItemAdmin )
