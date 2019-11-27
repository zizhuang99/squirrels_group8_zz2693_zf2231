from django.shortcuts import render

# Create your views here


from .models import squirrels


def plotid(request):
     squirrels_longitude = [float(a) for a in squirrels.objects.all().values_list('Longitude',flat=True)]
     squirrels_latitude = [float(a) for a in squirrels.objects.all().values_list('Latitude',flat=True)]
     context = {'squirrels_longitude': squirrels_longitude,
            'squirrels_latitude': squirrels_latitude,}
     return render(request, 'map/squirrels_map.html',context)
