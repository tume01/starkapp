from django.contrib import auth
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType



@require_http_methods(['POST'])
def login_view(request):
    
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
    return render(request, 'login.html') 

@require_http_methods(['GET'])
def index(request):	
    
    # Redirect to a success page.
    return render(request, 'login.html') 