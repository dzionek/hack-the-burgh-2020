from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        context = {}
        return render(request, 'pages/home.html', context)
    else:
        return HttpResponseRedirect('/global-map/')
