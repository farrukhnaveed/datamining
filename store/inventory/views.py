from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from store.inventory.models import Category, Item
# Create your views here.


def homepage( request, template_name ):
	return HttpResponseRedirect(reverse('category', args=['phones']))
	# return render_to_response(template_name, {'test': 'test'}, context_instance=RequestContext(request))


def category( request, category_slug, template_name ):
	categories = Category.objects.all()
	items = Item.objects.filter(category__slug=category_slug, status=True)
	message = cache.get('message')
	cache.set('message', None)
	
	context = {
		'categories': categories,
		'items': items,
		'message': message
	}
	return render_to_response(template_name, context, context_instance=RequestContext(request))


def sub_category( request, category_slug, sub_category_slug, template_name ):
	categories = Category.objects.all()
	items = Item.objects.filter(sub_category__slug=sub_category_slug, status=True)

	context = {
		'categories': categories,
		'items': items,
	}
	return render_to_response(template_name, context, context_instance=RequestContext(request))


def item( request, category_slug, sub_category_slug, item_slug, template_name ):
	categories = Category.objects.all()
	item = Item.objects.get(slug=item_slug)
	items = []

	print len(Item.objects.filter(tags__name__in=['phone accessories']))
	try:
		items.append(Item.objects.filter(tags__name__in=['phone accessories']).filter(tags__name__in=['bluetooth']).filter(tags__name__in=[item.sub_category.slug])[0])
	except:
		items.append(Item.objects.filter(sub_category=item.sub_category)[0])
	try:
		items.append(Item.objects.filter(tags__name__in=['phone accessories']).filter(tags__name__in=['covers']).filter(tags__name__in=[item.sub_category.slug])[0])
	except:
		items.append(Item.objects.filter(sub_category=item.sub_category)[1])
	try:
		items.append(Item.objects.filter(tags__name__in=['phone accessories']).filter(tags__name__in=['headphones']).filter(tags__name__in=[item.sub_category.slug])[0])
	except:
		items.append(Item.objects.filter(sub_category=item.sub_category)[2])
	
	# items= Item.objects.all()[0:3]
	#print items
	context = {
		'categories': categories,
		'item': item,
		'items': items,
	}
	return render_to_response(template_name, context, context_instance=RequestContext(request))
