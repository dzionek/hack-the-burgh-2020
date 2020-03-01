from django.shortcuts import render

from django.contrib.auth import logout
from .forms import RegistrationForm
# Create your views here.

def registration_view(request, *args, **kwargs):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'users/registration.html', context)

def logout_view(request):
    context = {}
    logout(request)
    return render(request, '', context)