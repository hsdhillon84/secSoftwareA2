#views.py
from secSoftwareA2.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf


@csrf_protect
def register(request):
  if request.method == 'POST':
    form = userCreation(request.POST)
    if form.is_valid():
      new_user = form.save()
      return HttpResponseRedirect('/register/success/')
  else:
    form = userCreation()
    c = {'form': form}
    return render_to_response('registration/register.html', c, context_instance=RequestContext(request))


def register_success(request):
  return render_to_response(
  'registration/success.html',
  )

@csrf_protect
def update(request):
  return render_to_response(
  'registration/update.html',
  { 'user': request.user }
  )

def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')
 
@login_required
def home(request):
  return render_to_response(
  'home.html',
  { 'user': request.user }
  )