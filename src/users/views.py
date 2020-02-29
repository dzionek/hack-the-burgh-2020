from django.shortcuts import render

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