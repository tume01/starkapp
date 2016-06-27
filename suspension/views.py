from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.MembershipService import MembershipService
from services.SuspensionService import SuspensionService
from datetime import datetime
from django.views.decorators.http import require_http_methods
from adapters.FormValidator import FormValidator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .forms import SuspensionForms
from services.MemberService import MembersService
from services.SuspensionTypeService import SuspensionTypeService
from django.contrib.auth.models import Group

@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def create_suspension_index(request):

    member_service = MembersService()

    memberId = request.POST['member_id']

    member = member_service.getMember(memberId)

    membership_id = member.membership.id

    membership_service = MembershipService()

    suspension_type_service = SuspensionTypeService()

    suspension_types = suspension_type_service.getSuspensionTypes()

    membership = membership_service.getMembership(membership_id)

    context = {
        'suspension_types' : suspension_types,
        'membership': membership,
        'member':member
    }

    return render(request, 'Admin/Suspension/new_suspension.html', context)

@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def create_suspension(request):

    membershipId = request.POST['membership_id']

    suspensionTypeId = request.POST['suspention_type_id']

    form = SuspensionForms(request.POST)

    if FormValidator.validateForm(form, request):

        membership_service = MembershipService()

        suspension_type_service = SuspensionTypeService()

        suspension_types = suspension_type_service.getSuspensionTypes()

        membership = membership_service.getMembership(membershipId)

        context = {
            'membership': membership,
            'suspension_types' : suspension_types
        }

        return render(request, 'Admin/Suspension/new_suspension.html', context)

    else:

        insert_data = {}

        insert_data['suspension_type_id'] = suspensionTypeId

        insert_data['membership_id'] = membershipId

        insert_data["reason"] = form.cleaned_data['reason']

        insert_data['initialDate'] = form.cleaned_data['initialDate']

        insert_data['finalDate'] = form.cleaned_data['finalDate']

        insert_data['status'] = 1

        admin_user = request.user

        insert_data['responsable'] = admin_user.first_name

        suspension_service = SuspensionService()

        suspension_service.create(insert_data)

        member_service = MembersService()

        filter_data = {}

        filter_data['membership_id'] = membershipId

        member = member_service.filter(filter_data)[0]

        current_user = member.user

        group = Group.objects.get(name='usuarios_suspendidos')

        group.user_set.add(current_user)

        return HttpResponseRedirect(reverse('members:index'))



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_suspension_index(request):

    suspension_id = request.POST['id']

    suspension_service = SuspensionService()

    suspension_type_service = SuspensionTypeService()

    suspension_types = suspension_type_service.getSuspensionTypes()

    suspension = suspension_service.getSuspension(suspension_id)

    suspension.initialDate = datetime.strftime(suspension.initialDate, '%m/%d/%Y')

    suspension.finalDate = datetime.strftime(suspension.finalDate, '%m/%d/%Y')

    context = {
        'suspension' : suspension,
        'suspension_types' : suspension_types
    }

    return render(request, 'Admin/Suspension/edit_suspension.html', context)

@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_suspension(request):

    suspension_id = request.POST['id_suspension']

    suspension_type_id = request.POST['suspension_type_id']

    suspension_service = SuspensionService()

    suspension_type_service = SuspensionTypeService()

    suspension = suspension_service.getSuspension(suspension_id)

    form = SuspensionForms(request.POST)

    if FormValidator.validateForm(form, request):

        suspension_types = suspension_type_service.getSuspensionTypes()

        context = {
            'suspension': suspension,
            'suspension_types' : suspension_types
        }

        return render(request, 'Admin/Suspension/edit_suspension.html', context)

    else:

        edit_data = {}

        edit_data['suspension_type_id'] = suspension_type_id

        edit_data["reason"] = form.cleaned_data['reason']

        edit_data['initialDate'] = form.cleaned_data['initialDate']

        edit_data['finalDate'] = form.cleaned_data['finalDate']

        suspension_service = SuspensionService()

        suspension_service.update(suspension_id, edit_data)

        return HttpResponseRedirect(reverse('members:index'))

@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def suspension_index(request):

    membership_service = MembershipService()

    member_service = MembersService()

    suspension_service = SuspensionService()

    memberId = request.POST['id']

    suspension_type_service = SuspensionTypeService()

    suspension_types = suspension_type_service.getSuspensionTypes()

    member = member_service.getMember(memberId)

    membershipId = member.membership.id

    filter_data = {}

    filter_data['membership_id'] = membershipId

    membership = membership_service.getMembership(membershipId)

    suspensions = suspension_service.filter(filter_data)

    show = not any(s.status == 1 for s in suspensions)

    context = {
        'id': membershipId,
        'suspensions': suspensions,
        'membership' : membership,
        'member' : member,
        'show' : show,
        'suspension_types' : suspension_types,
    }

    return render(request, 'Admin/Suspension/index_suspensions.html', context)

@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def suspension_filter(request):

    suspension_type_service = SuspensionTypeService()

    suspension_types = suspension_type_service.getSuspensionTypes()

    membership_service = MembershipService()

    member_service = MembersService()

    suspension_service = SuspensionService()

    memberId = request.POST['member_id']

    member = member_service.getMember(memberId)

    membershipId = member.membership.id

    membership = membership_service.getMembership(membershipId)

    filter_suspensions = {}

    suspStatus = request.POST['status']

    iniDate = request.POST['initialDate']

    endDate = request.POST['finalDate']

    suspension_type = request.POST['suspension_type']

    filter_suspensions['membership_id'] = membershipId

    if iniDate != '':
        filter_suspensions["initialDate__gte"] = datetime.strptime(iniDate, '%m/%d/%Y')

    if endDate != '':
        filter_suspensions["finalDate__lte"] = datetime.strptime(endDate, '%m/%d/%Y')

    if suspStatus != '3':
        filter_suspensions["status"] = suspStatus

    if suspension_type != 'Todos':
        filter_suspensions['suspension_type_id'] = suspension_type

    suspensions = suspension_service.filter(filter_suspensions)

    filter_all_suspensions = {}

    filter_all_suspensions['membership_id'] = membershipId

    all_Suspensions = suspension_service.filter(filter_all_suspensions)

    show = not any(s.status == 1 for s in all_Suspensions)

    context = {
        'id': membershipId,
        'suspensions': suspensions,
        'member' : member,
        'membership': membership,
        'show' : show,
        'suspension_types' : suspension_types,
    }

    return render(request, 'Admin/Suspension/index_suspensions.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def delete_suspension(request):
    edit_data = {}

    id_edit = request.POST['id']

    edit_data["status"] = 0

    suspension_service = SuspensionService()

    suspension_service.update(id_edit, edit_data)

    form = SuspensionForms(request.POST)

    member_service = MembersService()

    suspension = suspension_service.getSuspension(id_edit)

    filter_data = {}

    filter_data['membership_id'] = suspension.membership.id

    member = member_service.filter(filter_data)[0]

    current_user = member.user

    for group in current_user.groups.all():

        if group.name == 'usuarios_suspendidos':

            group.user_set.remove(current_user)
            break

    return HttpResponseRedirect(reverse('members:index'))
