from django.contrib import admin
from store.inventory.models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
    list_display =('name', 'slug')

class ItemAdmin(admin.ModelAdmin):
    list_display =('name', 'category', 'price', 'slug', 'status')


admin.site.register( Category, CategoryAdmin )
admin.site.register( Item, ItemAdmin )
