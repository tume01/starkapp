from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.MemberService import MembersService
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def member_index(request):

    member_service = MembersService()

    members = member_service.getMembers()

    context = {
        'members' : members,
    }

    return render(request, 'Admin/Members/index_members.html', context) 


@require_http_methods(['POST'])
def edit_member_index(request):

    id_member = request.POST['id']

    member_service = MembersService()

    member = member_service.getMember(id_member)

    context = {
        'member' : member,
    }

    return render(request, 'Admin/Members/edit_member.html', context)

@require_http_methods(['POST'])
def delete_member(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["state"] = 0

    member_service = MembersService()

    member_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('members:index'))


@require_http_methods(['POST'])
def edit_member(request):

    edit_data = {}

    edit_data["name"] = request.POST['name']

    edit_data["surname"] = request.POST['surname']

    edit_data["dni"] = request.POST['dni']

    edit_data["phone"] = request.POST['phone']

    edit_data["address"] = request.POST['address']

    edit_data["email"] = request.POST['email']

    id_edit = request.POST['id']

    member_service = MembersService()

    member_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('members:index'))
