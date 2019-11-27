from django.urls import path
from sightings.views import *

urlpatterns=[
        path('',index, name='sightings_list'),
        path('<str:sighting>/',details,name='sighting_detail'),
        path('add/',add,name='add_sighting'),
        ]
