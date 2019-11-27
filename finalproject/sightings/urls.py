from django.urls import path
from sightings.views import *

urlpatterns=[
        path('',index, name='sightings_list'),
        path('<str:Unique_Squirrel_Id>/',details,name='sighting_detail'),
        path('add/',add,name='add_sighting'),
        ]
