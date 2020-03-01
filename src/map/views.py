from django.http import HttpResponseRedirect
from django.shortcuts import render
import config
from map.forms import AddPlaceForm
from map.models import Patient
# Create your views here.
def add_place_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        # if length of POST is longer than just the token
        if len(request.POST) > 1:
            location = request.POST['WHERE']
            time = request.POST['WHEN']
            new_place = [location, time]
            for patient in Patient.objects.values():
                if patient['user_id'] == request.user.id:
                    patient['places_list'] += str(new_place)

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