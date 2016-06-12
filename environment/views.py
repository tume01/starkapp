from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.EnvironmentService import EnvironmentService
from django.views.decorators.http import require_http_methods
from .forms import EnvironmentForm

@require_http_methods(['GET'])
def index(request):

    environment_service = EnvironmentService()

    environments = environment_service.getEnvironmentByStatus()

    context = {
        'environments' : environments,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Environments/List_Environment.html', context)

@require_http_methods(['GET'])
def create_index(request):

    form = EnvironmentForm()
    context = {
        'titulo' : 'titulo',
        'form' : form
    }

    return render(request, 'Admin/Environments/Create_Environment.html', context)

@require_http_methods(['GET'])
def edit_index(request, id):

    environment_service = EnvironmentService()

    environments = environment_service.getEnviromentById(id)
    print(id)
    #Falta validación de try except dentro de base repository
    if (environments == None):
        return HttpResponseRedirect(reverse('Environments:index'))

    form = EnvironmentForm(instance=environments)
    context = {
		'id' :id,
        'form' : form,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Environments/Edit_Environment.html', context)

@require_http_methods(['POST'])
def delete_environment(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["status"] = 0

    environment_service = EnvironmentService()

    environment_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('environment:index'))


@require_http_methods(['POST'])
def create_environment(request):
    if request.POST:
        form = EnvironmentForm(request.POST)
        
        if form.is_valid():
            print("pasa")
            insert_data = {}
            insert_data["name"] = request.POST['name']
            insert_data["capacity"] = request.POST['capacity']
            insert_data["status"] = request.POST['status']
            #insert_data["headquarter"] = request.POST['headquarter']
            insert_data["description"] = request.POST['description']
                
            environment_service = EnvironmentService()

            environment_service.create(insert_data)

            return HttpResponseRedirect(reverse('environment:index'))

        else:

            errors = form.errors.as_data()
            for error in errors:
                print(error)
            context = {'form' : form}
            return render(request, 'Admin/Environments/Create_Environment.html', context)


@require_http_methods(['POST'])
def edit_environment(request, id):
    if request.POST:
        form = EnvironmentForm(request.POST)
        
        if form.is_valid():

            #form.save()

            insert_data = {}
            insert_data["name"] = request.POST['name']
            insert_data["capacity"] = request.POST['capacity']
            insert_data["status"] = request.POST['status']
            #insert_data["headquarter"] = request.POST['headquarter']
            insert_data["description"] = request.POST['description']

            environment_service = EnvironmentService()

            environment_service.update(id, insert_data)

            return HttpResponseRedirect(reverse('environment:index'))
        else:

            errors = form.errors.as_data()
            for error in errors:
                print(error)
            context = {'form' : form}
            return render(request, 'Admin/Environments/Edit_Environment.html', context)
