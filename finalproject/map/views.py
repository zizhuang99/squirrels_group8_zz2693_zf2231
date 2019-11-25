from django.shortcuts import render

# Create your views here


from .models import squirrels


def plotid(request):
#    squirrels_longitude = squirrels.objects.all().values_list('Longitute')
#    squirrels_longitude = squirrels.objects.all().values_list('Latitude')
#    context = {'squirrels_longitude': squirrels_longitude;
#           'squirrels_latitude': squirrels_latitude}
    return render(request, 'map/squirrels_map.html')
