from django.http import HttpResponseRedirect
from django.shortcuts import render
import config
from map.forms import AddPlaceForm
# Create your views here.
def add_place_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddPlaceForm(request.POST)
            if form.is_valid():
                location = form.cleaned_data['location']
                time = form.cleaned_data['time']
                print(location, time)

        form = AddPlaceForm()
        context = {
            'api_key': config.api_key,
            'form': form
        }
        return render(request, 'map/add-place.html', context)
    else:
        return HttpResponseRedirect('/')

def global_map_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'map/global-map.html', context)
    else:
        return HttpResponseRedirect('/')