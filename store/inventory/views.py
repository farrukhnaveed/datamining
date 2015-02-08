from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.


def homepage( request, template_name ):
	test = 'Hello my name is farrukh'

	context = {
		"test": test,
	}
	return render_to_response(template_name, context, context_instance=RequestContext(request))
