from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Location
import requests

@login_required
def index(request):
    location_list = Location.objects.filter(uname=request.user.username)
    weather_data_list = []
    for location in location_list:
        r = requests.get("http://api.wunderground.com/api/2569783e0528aa2d/geolookup/conditions/q/{}.json".format(location.zip_code))
        response_data = r.json()
        conditions = response_data['current_observation']
        weather_data = {
                'location': conditions['display_location']['full'],
                'zip': conditions['display_location']['zip'],
                'temp_string': conditions['temperature_string'],
                'humidity': conditions['relative_humidity'],
        }
        weather_data_list.append(weather_data)
                
    context = {'location_list': weather_data_list}
    return render(request, "weather_app/index.html", context)

def new_location(request):
    loc = request.POST['zip']
    l = Location(uname=request.user.username, zip_code=loc)
    l.save()
    return redirect('index')
