from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from services.EntryService import EntryService


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def index(request):

    context = {
        'entries' : entries,
    }

    return render(request, 'Admin/Guests/index_promotion.html', context) 


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Guests/new_guests_members.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def insert(request):

    edit_data = {}

    return HttpResponseRedirect(reverse('entry:index'))