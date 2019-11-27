from django.shortcuts import render
from django.http import HttpResponse
from map.models import squirrels


def index(request):
    sightings=squirrels.objects.all()
    context={'sightings':sightings,} 
    return render(request,"sightings/index.html",context)
# Create your views here.
def details(request,Unique_Squirrel_Id=None):
    sighting2=squirrels.objects.get(Unique_Squirrel_Id=sighting)
    context={'sighting':sighting2,}
    return render(request,"sightings/details.html",context)
def add(request,Unique_Squirrel_Id=None):
    if request.method=="POST":
        print(request.POST)
        data=request.POST
        

        ret=squirrels.objects.create(Unique_Squirrel_Id='123',longitude=data['longitutde'])
        if ret:
            return HttpResponse('Your answer has been recorded successfully')
        else:
            return HttpResponse("Your answer hasn't been recorded")
   # if request.method=="GET":
    #    try:
     #       sighting=Sightings.object.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
      #  context={'sighting':sighting,}
       # return render(request,sightings/add.html.context)
