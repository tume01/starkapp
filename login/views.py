from django.contrib import auth
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User, Group



@require_http_methods(['POST'])
def login_view(request):
    
    """
    user1 = User.objects.create_user(username='usuario', password='1111')
    user2 = User.objects.create_user(username='administrador', password='1111')
    user3 = User.objects.create_user(username='bungalow', password='1111')
    user4 = User.objects.create_user(username='evento', password='1111')
    user5 = User.objects.create_user(username='cancha', password='1111')
    user6 = User.objects.create_user(username='cajero', password='1111')
    user7 = User.objects.create_user(username='membresia', password='1111')
    user8 = User.objects.create_user(username='empresa', password='1111')

    usuario = Group.objects.create(name='usuarios')
    admin = Group.objects.create(name='admins')
    bungalows = Group.objects.create(name='bungalows')
    eventos = Group.objects.create(name='eventos')
    canchas = Group.objects.create(name='canchas')
    cajero = Group.objects.create(name='cajeros')
    membresia = Group.objects.create(name='membresias')
    empresa = Group.objects.create(name='empresas')

    usuario.user_set.add(user1)
    admin.user_set.add(user2)
    bungalows.user_set.add(user3)
    eventos.user_set.add(user4)
    canchas.user_set.add(user5)
    cajero.user_set.add(user6)
    membresia.user_set.add(user7)
    empresa.user_set.add(user8)
    """


    username = request.POST['username']
    password = request.POST['password']
    print(username, password)
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect(reverse("memberships:type/index"))
    else:
        # Show an error page
    	return HttpResponseRedirect(reverse("login.html"))



@require_http_methods(['GET'])
def logout_view(request):

    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")

@require_http_methods(['GET'])
def index(request):	
    
    # Redirect to a success page.
    return render(request, 'login.html') 