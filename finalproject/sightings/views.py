from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from map.models import squirrels
from django.views.generic.edit import CreateView,UpdateView,DeleteView


def index(request):
    sightings=squirrels.objects.all()
    context={'sightings':sightings,} 
    return render(request,"sightings/index.html",context)
# Create your views here.
def details(request,Unique_Squirrel_ID):
    sighting=squirrels.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    context={'sighting':sighting,}
    return render(request,"sightings/details.html",context)

def stats(request):
    stats1=squirrels.objects.all().count()
    stats2=squirrels.objects.filter(Runs_from=True).count()
    stats3=squirrels.objects.filter(Climbing=True).count()
    stats4=squirrels.objects.filter(Primary_fur_color='Black').count()
    stats5=squirrels.objects.filter(Chasing=True).count()
    context={'stats1':stats1,'stats2':stats2,'stats3':stats3,'stats4':stats4,'stats5':stats5,}
    return render(request,'sightings/stats.html',context)
def add(request):
    if request.method=="POST":
    #print("Add sightings to the databse")
        Unique_Squirrel_ID = request.POST.get('Unique_Squirrel_ID')
        Longitude = request.POST.get('Longitude')
        Latitude=request.POST.get('Latitude')
        Specific_location=request.POST.get('Specific_location')
        Date=request.POST.get('Date')
        Shift=request.POST.get('Shift')
        Age=request.POST.get('Age')
        Primary_fur_color=request.POST.get('Primary_fur_color')
        Location=request.POST.get('Location')
        Running=request.POST.get('Running')
        Chasing=request.POST.get('Chasing')
        Climbing=request.POST.get('Climbing')
        Eating=request.POST.get('Eating')
        Foraging=request.POST.get('Foraging')
        Other_Activities=request.POST.get('Other_Activities')
        Kuks=request.POST.get('Kuks')
       
        Quaas=request.POST.get('Quaas')
        Moans=request.POST.get('Moans')
        Tail_flags=request.POST.get('Tail_flags')
        Tail_twitches=request.POST.get('Tail_twitches')
        Approaches=request.POST.get('Approaches')
        Indifferent=request.POST.get('Indifferent')

        squirrel=squirrels.objects.create(Unique_Squirrel_ID=Unique_Squirrel_ID,
                Longitude=Longitude,Latitude=Latitude,Specific_location=Specific_location,
                Date=Date,Shift=Shift,Age=Age, Primary_fur_color=Primary_fur_color,
                Location=Location, 
                Running=Running,Chasing=Chasing,
                Climbing=Climbing,Eating=Eating,Foraging=Foraging,Other_Activities=Other_Activities,
                Kuks=Kuks,Quaas=Quaas,Moans=Moans,Tail_flags=Tail_flags,Tail_twitches=Tail_twitches,Approaches=Approaches, Indifferent=Indifferent)
        
        squirrel.save()
        return redirect('sightings:index')
    return render(request,'sightings/add.html')


def delete(request, Unique_Squirrel_ID):
    sighting=squirrels.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=='POST':
        sighting.delete()
        return redirect('sightings:index')
    else:
        context={'sighting':sighting}
        return(render(request,'sightings/delete.html',context))



def update(request, Unique_Squirrel_ID):
 #   print("Update method in address_book views.py")

# updating user information
    sighting = squirrels.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=="POST":
        sighting.Longitude=request.POST['Longitude']
        sighting.Latitude=request.POST['Latitude']
        sighting.Shift=request.POST['Shift']
        sighting.Date=request.POST['Date']
        sighting.Age=request.POST['Age']
        sighting.Primary_fur_color=request.POST['Primary_fur_color']
        sighting.Location=request.POST['Location']
        sighting.Specific_location=request.POST['Specific_location']
        sighting.Running=request.POST['Running']
        sighting.Chaseing=request.POST['Chasing']
        sighting.Climbing=request.POST['Climbing']
        sighting.Eating=request.POST['Eating']
        sighting.Foraging=request.POST['Foraging']
        sighting.Other_Activities=request.POST['Other_Activities']
        sighting.Kuks=request.POST['Kuks']
        sighting.Quaas=request.POST['Quaas']
        sighting.Moans=request.POST['Moans']
        sighting.Tail_flags=request.POST['Tail_flags']
        sighting.Tail_twitches=request.POST['Tail_twitches']
        sighting.Approaches=request.POST['Approaches']
        sighting.Indifferent=request.POST['Indifferent']
        sighting.Runs_from=request.POST['Runs_from']
       # sighting.save()
        context={'sighting':sighting}
        return render(request,'sightings/details.html', context)

    context={'sighting':sighting}

    return render(request,'sightings/update.html',context)


