from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.MemberService import MembersService
from django.views.decorators.http import require_http_methods
from services.IdentityDocumentTypeService import IdentityDocumentTypeService
from Adapters.FormValidator import FormValidator
from .forms import  MemberForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['GET'])
def member_index(request):

    member_service = MembersService()

    members = member_service.getMembers()

    context = {
        'members' : members,
    }

    return render(request, 'Admin/Members/index_members.html', context) 


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_member_index(request):

    id_member = request.POST['id']

    member_service = MembersService()

    member = member_service.getMember(id_member)

    identity_document_type_service = IdentityDocumentTypeService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    context = {
        'member' : member,
        'doc_types': doc_types,
    }

    return render(request, 'Admin/Members/edit_member.html', context)



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def delete_member(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["state"] = 0

    member_service = MembersService()

    member_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('members:index'))




@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_member(request):

    form = MemberForm(request.POST)

    id_edit = request.POST['id']

    identity_doc_type = request.POST['identity_document_type']

    if FormValidator.validateForm(form, request):

        member_service = MembersService()

        member = member_service.getMember(id_edit)

        identity_document_type_service = IdentityDocumentTypeService()

        doc_types = identity_document_type_service.getIdentityDocumentTypes()

        context = {
            'member': member,
            'doc_types': doc_types
        }

        return render(request, 'Admin/Members/edit_member.html', context)

    else:

        edit_data = {}

        edit_data["identity_document_type_id"] = identity_doc_type

        edit_data["name"] = form.cleaned_data['name']

        edit_data["paternalLastName"] = form.cleaned_data['paternalLastName']

        edit_data["maternalLastName"] = form.cleaned_data['maternalLastName']

        edit_data["document_number"] = form.cleaned_data['num_doc']

        edit_data["phone"] = form.cleaned_data['phone']

        edit_data["address"] = form.cleaned_data['address']

        edit_data["email"] = form.cleaned_data['email']

        member_service = MembersService()

        member_service.update(id_edit, edit_data)

        return HttpResponseRedirect(reverse('members:index'))
