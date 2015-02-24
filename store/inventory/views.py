from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from store.inventory.models import Category, Item
# Create your views here.


def homepage( request, template_name ):
	return HttpResponseRedirect(reverse('category', args=['phones']))
	# return render_to_response(template_name, {'test': 'test'}, context_instance=RequestContext(request))


def category( request, category_slug, template_name ):
	categories = Category.objects.all()
	items = Item.objects.filter(category__slug=category_slug, status=True)


	context = {
		'categories': categories,
		'items': items,
	}
	return render_to_response(template_name, context, context_instance=RequestContext(request))


def item( request, category_slug, item_slug, template_name ):
	categories = Category.objects.all()
	item = Item.objects.get(slug=item_slug)
	items= Item.objects.all()[0:3]
	context = {
		'categories': categories,
		'item': item,
		'items': items,
	}
	return render_to_response(template_name, context, context_instance=RequestContext(request))
