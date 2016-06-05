from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from services.ServiciosService import ServiciosService
from django.views.decorators.http import require_http_methods

# Create your views here.


@require_http_methods(['GET'])
def index(request):

    servicios_service = ServiciosService()

    filters = {
    	'servicio_type_id' : 1
    }

    fields = servicios_service.filter(filters)

    context = {
        'fields' : fields,
        'titulo' : 'titulo'
    }

    return render(request, 'User/Reservation/fields.html', context)
