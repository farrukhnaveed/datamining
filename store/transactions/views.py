from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from store.inventory.models import Item
from store.transactions.models import Transaction, TransactionItem
# Create your views here.


def add_item(request):
	if request.is_ajax():
		if request.method == 'GET':
			item_id = request.GET.get('item_id', None)
			quantity = request.GET.get('quantity', '1')
			
			try:
				item_id = int(item_id)
				quantity = int(quantity)
			except TypeError, ValueError:
				return HttpResponse('Invalid Data')

			# todo: need to verify id
			# cache.clear()	
			cache_key = 'cart'
			bucket = cache.get(cache_key)
			if bucket:
				bucket.append(item_id)
			else:
				bucket = [item_id]
			cache.set(cache_key, bucket)

			cart = {'bucket' : bucket}
			return HttpResponse ( simplejson.dumps(cart), mimetype = 'application/json' )
		else:
			return HttpResponse('Invalid method')		
	else:
		return HttpResponse('Invalid URL')

def cart(request, template_name):
	total = 0
	cache_key = 'cart'
	bucket = cache.get(cache_key)

	if bucket:
		items = Item.objects.filter(id__in = bucket)
		total = 0
		for item in items:
			total = total + item.price
	else:
		items = None 
	context = {
		'items': items,
		'total': total
	}
	return render_to_response(template_name, context, context_instance=RequestContext(request))

def checkout(request):
	if request.user.is_authenticated():
		user = User.objects.get(username = request.user.username)
		cache_key = 'cart'
		bucket = cache.get(cache_key)
		cache.clear()
		if bucket:
			items = Item.objects.filter(id__in = bucket)
			total = 0
			for item in items:
				total = total + item.price
			transaction = Transaction()
			transaction.user = user
			transaction.total_price = total
			transaction.save()
			for item in items:
				transaction_item = TransactionItem()
				transaction_item.item = item
				transaction_item.quantity = 1
				transaction_item.transaction = transaction
				transaction_item.save()
			cache.set('message', 'success')
		else:
			items = None 
			cache.set('message', 'error')
	else:
		return HttpResponseRedirect(reverse('auth_login')+'?next='+reverse('checkout'))
	return HttpResponseRedirect(reverse('category', args=['phones']))