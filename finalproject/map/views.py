from django.shortcuts import render

# Create your views here


from .models import squirrels


def squirrels_map(request):
    sightings=squirrels.objects.all()[:100]
    
    return render(request, 'map/squirrels_map.html',{'sightings':sightings})
