from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from Adapters.FormValidator import FormValidator
from .forms import UserForm, UserTypeForm
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from services.Membership_ApplicationService import Membership_ApplicationService
from services.MemberService import MembersService
from services.AffiliateService import AffiliateService


#TIPOS DE USUARIO
@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def user_type_index(request):

    groups = Group.objects.all()

    context = {
        'groups' : groups,
    }

    return render(request, 'Admin/Users/index_type_user.html', context) 


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def create_user_type_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Users/new_type_user.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def edit_user_type_index(request):

    id_type = request.POST['id']

    group = Group.objects.get(id=id_type)

    context = {
        'group' : group,
    }

    return render(request, 'Admin/Users/edit_type_user.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def create_user_type(request):

    form = UserTypeForm(request.POST)

    request = FormValidator.validateForm(form, request)

    if not request:

        insert_data = {}

        name = form.cleaned_data['name']

        Group.objects.create(name=name)

        return HttpResponseRedirect(reverse('users:type/index'))

    else:

        context = {
            'titulo' : 'titulo'
        }

        return render(request, 'Admin/Users/new_type_user.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def edit_user_type(request):

    form = UserTypeForm(request.POST)

    id_edit = request.POST['id']

    if FormValidator.validateForm(form, request):

        group = Group.objects.get(id=id_edit)

        context = {
            'group' : group
        }

        return render(request, 'Admin/Users/edit_type_user.html', context)

    else:

        name = form.cleaned_data['name']

        group = Group.objects.get(id=id_edit)

        group.name = name

        group.save()

        return HttpResponseRedirect(reverse('users:type/index'))



#USUARIOS
@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def edit_user_member(request):

    id_member = request.POST['id']

    member_service = MembersService()

    member = member_service.getMember(id_member)

    user = User.objects.get(id=member.user_id)

    groups = Group.objects.all()

    user.type = user.groups.all()[0].id

    context = {
        'user' : user,
        'groups' : groups,
    }

    return render(request, 'Admin/Users/edit_user.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def edit_user_index(request):

    id_user = request.POST['id']

    user = User.objects.get(id=id_user)

    groups = Group.objects.all()

    user.type = user.groups.all()[0].id

    context = {
        'user' : user,
        'groups' : groups,
    }

    return render(request, 'Admin/Users/edit_user.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def edit_user(request):

    form = UserForm(request.POST)

    id_edit = request.POST['id']

    if FormValidator.validateForm(form, request):

        user = User.objects.get(id=id_edit)

        user.type = user.groups.all()[0].id

        groups = Group.objects.all()

        context = {
            'user' : user,
            'groups' : groups,
        }

        return render(request, 'Admin/Users/edit_user.html', context)

    else:

        user = User.objects.get(id=id_edit)

        user.username = form.cleaned_data['name']

        user.set_password(form.cleaned_data['password'])

        user.save()

        group = Group.objects.get(id=(form.cleaned_data['user_type']))

        user.groups.all()[0].user_set.remove(user)
     
        group.user_set.add(user)

        return HttpResponseRedirect(reverse('users:index'))

#user
@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')
@require_http_methods(['POST'])
def edit_password(request):
    user = User.objects.get(id=id_edit)
    user.set_password(form.cleaned_data['password'])
    user.save()
    return HttpResponseRedirect(reverse('users:password'))

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def create_user_index(request):

    groups = Group.objects.all()

    context = {
        'titulo' : 'titulo',
        'groups' : groups,
    }

    return render(request, 'Admin/Users/new_user.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def create_user(request):

    form = UserForm(request.POST)

    request = FormValidator.validateForm(form, request)

    if not request:

        name = form.cleaned_data['name']

        password = form.cleaned_data['password']

        group = Group.objects.get(id=(form.cleaned_data['user_type']))

        user = User.objects.create_user(username=name, password=password)

        group.user_set.add(user)

        return HttpResponseRedirect(reverse('users:index'))

    else:

        groups = Group.objects.all()

        context = {
            'titulo' : 'titulo',
            'groups' : groups
        }

        return render(request, 'Admin/Users/new_user.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def user_index(request):

    users = User.objects.all()

    context = {
        'users' : users,
    }

    return render(request, 'Admin/Users/index_user.html', context) 

@login_required
@require_http_methods(['POST'])
def verify_user(request):

    try:

        if(request.POST['username'] == request.POST['user']):

            return  HttpResponse("true")

        if( User.objects.get(username=(request.POST['username']))):
     
            return  HttpResponse("false")

    except User.DoesNotExist:

        pass

    try:

        if request.POST['username'].isdigit():
            
            return HttpResponse("false")

        return  HttpResponse("true")

    except ValueError:

        return  HttpResponse("true")



@login_required
@require_http_methods(['POST'])
def verify_user_member(request):

    try:

        if( User.objects.get(username=(request.POST['username']))):

            member_service = MembersService()

            member = member_service.getMember(request.POST['id_member'])

            user = User.objects.get(username=(request.POST['username']))

            if(member.user_id == user.id):

                return  HttpResponse("true")
     
            return  HttpResponse("false")


    except User.DoesNotExist:

        member_application_service = Membership_ApplicationService()

        affiliate_service = AffiliateService()

        filter_data = {}

        filter_data["document_number"] = request.POST['username']

        filter_data["status"] = 1

        filter_data2 = {}

        filter_data2["document_number"] = request.POST['username']

        filter_data2["state"] = 1

        if( member_application_service.filter(filter_data)):

            return  HttpResponse("false")

        if( affiliate_service.filter(filter_data2)):

            return  HttpResponse("false")

        return  HttpResponse("true")
