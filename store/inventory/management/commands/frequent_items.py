from django.core.management.base import NoArgsCommand
from store.inventory.models import Item, FrequentItem
from store.transactions.models import Transaction, TransactionItem
from fp_growth import find_frequent_itemsets

class Command(NoArgsCommand):
    help = 'Find Frequent Itemsets'

    def handle_noargs(self, **options):
        support = 0
        all_items = []
        for transaction in Transaction.objects.all():
            items = TransactionItem.objects.filter(transaction=transaction).values_list('item__id', flat=True)
            all_items.append(map(str, items))


        while True:            
            items = {}
            itemsets = []
            for itemset, support in find_frequent_itemsets(all_items, support, True):
                itemsets.append(itemset)
                for item in itemset:
                    if int(item) not in items.keys():
                        items[item] = []

            for index in items.keys():
                for itemset in itemsets:
                    if index in itemset:
                        for item in itemset:
                            if item != index and item not in items[index]:
                                items[index].append(item)

            for main_item in items.keys():
                if len(items[main_item]) > 0:
                    for frequent_item in items[main_item]:
                        try:
                            item_set = FrequentItem.objects.get(main_item__id=int(main_item), frequent_item__id=int(frequent_item))
                        except:
                            item_set = FrequentItem()
                            item_set.main_item = Item.objects.get(id=int(main_item))
                            item_set.frequent_item = Item.objects.get(id=int(frequent_item))

                        item_set.support = support
                        item_set.save()

            print 'SUPPORT:', support
            print 'ITEMS:', items
            support += 1
            if len(items) < 1:
                break