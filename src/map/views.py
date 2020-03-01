from django.http import HttpResponseRedirect
from django.shortcuts import render
import config
from map.forms import AddPlaceForm
from map import models as map_models
# Create your views here.
def add_place_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        # if length of POST is longer than just the token
        if len(request.POST) > 1:
            location = request.POST['WHERE']
            time = request.POST['WHEN']
            new_place = (location, time)

            print(new_place)

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