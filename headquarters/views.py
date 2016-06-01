from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.HeadquarterService import HeadquarterService

from adapters.FormValidator import FormValidator
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import HeadquarterForm

# Create your views here.



@require_http_methods(['GET'])
def index(request):

	headquarter_service = HeadquarterService()
	
	headquarters = headquarter_service.getHeadquarters()

	context = {
		'headquarters': headquarters
	}

	return render(request, 'Admin/Headquarters/index_headquarter.html', context)



@require_http_methods(['GET'])
def create_headquarters_index(request):
	headquarter_service = HeadquarterService()

	headquarters = headquarter_service.getHeadquarters()

	context = {		
		'headquarters': headquarters
	}
	
	return render(request, 'Admin/Headquarters/new_headquarter.html', context)




@require_http_methods(['GET'])
def update_headquarters_index(request):
	headquarter_service = HeadquarterService()

	headquarters = headquarter_service.getHeadquarters()

	context = {		
		'headquarters': headquarters
	}
	
	return render(request, 'Admin/Headquarters/edit_headquarter.html', context)




@require_http_methods(['POST'])
def create_headquarters(request):

	form = HeadquarterForm(request.POST)

	new_id = request.POST['id']

	if not FormValidator.validateForm(form, request):
		
		insert_data = {}

		insert_data["name"] = form.cleaned_data['name']

		insert_data["location"] = form.cleaned_data['location']

		insert_data["description"] = form.cleaned_data['description']

		headquarter_service.create(insert_data)
		
		return HttpResponseRedirect(reverse('headquarters:index'))

	else:
		headquarter_service = HeadquarterService()

		headquarters = headquarter_service.getHeadquarters()

		context = {		
			'headquarters': headquarters
		}
		
		return render(request, 'Admin/Headquarters/new_headquarter.html', context)




@require_http_methods(['POST'])	
def update(request):
	
	form = HeadquarterForm(request.POST)
	
	id_edit = request.POST['id']

	if FormValidator.validateForm(form, request):
		
		Headquarter_service = HeadquarterService()

		headquarter = headquarter_service.findHearquarter(id_edit)

		context = {
			'headquarter': headquarter
		}

		return render(request, 'Admin/Headquarters/edit_headquarter.html', context)

	else:
		
		edit_data = {}

		edit_data["name"] = form.cleaned_data['name']

		edit_data["location"] = form.cleaned_data['location']		

		edit_data["description"] = form.cleaned_data['description']

		return HttpResponseRedirect(reverse('headquarter:index'))