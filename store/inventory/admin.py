from django.contrib import admin
from store.inventory.models import Category, SubCategory, Brand, Item, FrequentItem


class CategoryAdmin(admin.ModelAdmin):
    list_display =('name', 'slug')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display =('name', 'category', 'slug')


class BrandAdmin(admin.ModelAdmin):
    list_display =('name', 'slug')


class ItemAdmin(admin.ModelAdmin):
    list_display =('name', 'sub_category', 'price', 'slug', 'status')


class FrequentItemAdmin(admin.ModelAdmin):
    list_display =('main_item', 'frequent_item', 'support')


admin.site.register( Category, CategoryAdmin )
admin.site.register( SubCategory, SubCategoryAdmin )
admin.site.register( Brand, BrandAdmin )
admin.site.register( Item, ItemAdmin )
admin.site.register( FrequentItem, FrequentItemAdmin )
