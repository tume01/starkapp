from django.contrib import auth
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required



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
        return HttpResponseRedirect(reverse('login:ini'))
    else:
        # Show an error page
    	return HttpResponseRedirect(reverse("login:index"))



@require_http_methods(['GET'])
def logout_view(request):

    auth.logout(request)
    return render(request, 'login.html') 

@require_http_methods(['GET'])
def index(request):	
    
    # Redirect to a success page.
    return render(request, 'login.html') 


@login_required
@require_http_methods(['GET'])
def ini(request): 
    
    # Redirect to a success page.
    return render(request, 'User/starting_screen.html')