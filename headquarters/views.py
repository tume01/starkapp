from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from HeadquartesService import HeadquartesService

from adapters.FormValidator import FormValidator
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@require_http_methods(['GET'])
def index(request):
	headquartes_service = HeadquartesService()

def create_headquarters(request):
	request = FormValidator.validateForm(form, request)

	if not request:
		name = form.cleaned_data['name']
		location = form.cleaned_data['location']

		insert_data = {
			'name': name,
			'location': location,
		}

		headquartes_service.create(insert_data)

		return HttpResponseRedirect(reverse('TBD'))
	else
		return render(request, 'TBD', context)