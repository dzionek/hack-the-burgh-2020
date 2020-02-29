from django.shortcuts import render
import config
# Create your views here.
def add_place_view(request, *args, **kwargs):
    context = {'api_key': config.api_key}
    return render(request, 'map/add-place.html', context)
