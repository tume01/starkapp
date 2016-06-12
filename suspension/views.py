from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.MembershipService import MembershipService
from services.SuspensionService import SuspensionService
from datetime import datetime
from django.views.decorators.http import require_http_methods
from Adapters.FormValidator import FormValidator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .forms import SuspensionForms
from services.MemberService import MembersService

@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def create_suspension_index(request):

    membership_id = request.POST['membership_id']

    membership_service = MembershipService()

    membership = membership_service.getMembership(membership_id)

    member_service = MembersService()

    filter_member = {}

    filter_member["membership"] =membership

    member = member_service.filter(filter_member)

    context = {
        'membership': membership,
        'member':member[0]
    }

    return render(request, 'Admin/Suspension/new_suspension.html', context)

@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def create_suspension(request):

    membershipId = request.POST['membership_id']

    form = SuspensionForms(request.POST)

    if FormValidator.validateForm(form, request):

        membership_service = MembershipService()

        membership = membership_service.getMembership(membershipId)

        context = {
            'membership': membership,
        }

        return render(request, 'Admin/Suspension/new_suspension.html', context)

    else:

        insert_data = {}

        insert_data['membership_id'] = membershipId

        insert_data["reason"] = form.cleaned_data['reason']

        insert_data['initialDate'] = form.cleaned_data['initialDate']

        insert_data['finalDate'] = form.cleaned_data['finalDate']

        insert_data['status'] = 1

        suspension_service = SuspensionService()

        suspension_service.create(insert_data)

        return HttpResponseRedirect(reverse('members:index'))



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_suspension_index(request):

    suspension_id = request.POST['id']

    suspension_service = SuspensionService()

    suspension = suspension_service.getSuspension(suspension_id)

    suspension.initialDate = datetime.strftime(suspension.initialDate, '%m/%d/%Y')

    suspension.finalDate = datetime.strftime(suspension.finalDate, '%m/%d/%Y')

    context = {
        'suspension' : suspension,
    }

    return render(request, 'Admin/Suspension/edit_suspension.html', context)

@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_suspension(request):

    suspension_id = request.POST['id_suspension']

    suspension_service = SuspensionService()

    suspension = suspension_service.getSuspension(suspension_id)

    form = SuspensionForms(request.POST)

    if FormValidator.validateForm(form, request):

        context = {
            'suspension': suspension,
        }

        return render(request, 'Admin/Suspension/edit_suspension.html', context)

    else:

        edit_data = {}

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

    suspension_service = SuspensionService()

    membershipId = request.POST['id']

    filter_data = {}

    filter_data['membership_id'] = membershipId

    membership = membership_service.getMembership(membershipId)

    suspensions = suspension_service.filter(filter_data)

    show = not any(s.status == 1 for s in suspensions)

    context = {
        'id': membershipId,
        'suspensions': suspensions,
        'membership' : membership,
        'show' : show
    }

    return render(request, 'Admin/Suspension/index_suspensions.html', context)

@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def suspension_filter(request):

    suspension_service = SuspensionService()

    membership_service = MembershipService()

    membershipId = request.POST['membership_id']

    membership = membership_service.getMembership(membershipId)

    filter_suspensions = {}

    suspStatus = request.POST['status']

    iniDate = request.POST['initialDate']

    endDate = request.POST['finalDate']

    filter_suspensions['membership_id'] = membershipId

    if iniDate != '':
        filter_suspensions["initialDate"] = datetime.strptime(iniDate, '%m/%d/%Y')

    if endDate != '':
        filter_suspensions["finalDate"] = datetime.strptime(endDate, '%m/%d/%Y')

    if suspStatus != '3':
        filter_suspensions["status"] = suspStatus

    suspensions = suspension_service.filter(filter_suspensions)

    filter_all_suspensions = {}

    filter_all_suspensions['membership_id'] = membershipId

    all_Suspensions = suspension_service.filter(filter_all_suspensions)

    show = not any(s.status == 1 for s in all_Suspensions)

    context = {
        'id': membershipId,
        'suspensions': suspensions,
        'membership': membership,
        'show' : show
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

    return HttpResponseRedirect(reverse('members:index'))