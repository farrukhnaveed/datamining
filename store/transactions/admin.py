from django.contrib import admin
from store.transactions.models import Transaction, TransactionItem


class TransactionAdmin(admin.ModelAdmin):
    list_display =('user', 'total_price', 'datetime')

class TransactionItemAdmin(admin.ModelAdmin):
    list_display =('item', 'quantity', 'transaction')


admin.site.register( Transaction, TransactionAdmin )
admin.site.register( TransactionItem, TransactionItemAdmin )
