from datetime import datetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.db import models

from store.inventory.models import Item


# Create your models here.


class Transaction( models.Model ):
	user = models.ForeignKey(User, verbose_name="Customer")
	total_price = models.DecimalField( verbose_name="Total Price", max_digits=8, decimal_places=2)
	datetime = models.DateTimeField( verbose_name="Date-Time", default=datetime.now, blank = True)
	
	class Meta:
		verbose_name = "Transaction"
		verbose_name_plural = "Transactions"
		
	def __unicode__(self):
		return _(u'%s') % (self.datetime)


class TransactionItem( models.Model ):
	item = models.ForeignKey(Item, verbose_name="Item")
	transaction = models.ForeignKey(Transaction, verbose_name="Transaction")
	quantity = models.PositiveIntegerField( verbose_name="Item Quantity", max_length = 10, default=1)
	
	class Meta:
		verbose_name = "Transaction Item"
		verbose_name_plural = "Transaction Items"
		
	def __unicode__(self):
		return _(u'%s') % (self.transaction)