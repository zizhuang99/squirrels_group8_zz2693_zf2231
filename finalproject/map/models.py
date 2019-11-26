from django.db import models
from django.utils.translation import gettext as _

class squirrels(models.Model):
    Longitude= models.DecimalField(help_text='Longitude',max_digits=16,decimal_places=13)
    
    Latitude=models.DecimalField(help_text='Latitude',max_digits=16,decimal_places=13)
    
    Unique_Squirrel_ID=models.CharField(help_text='Unique Squirrel ID',max_length=200,)
    
  #  AM,PM='AM','PM'
   # Shift=models.CharField(help_text='Shift',max_length=200, choices=((AM,'am'),(PM,'pm'),))
    
    #Date=models.DateField(help_text='Date',max_length=200)
    
   # adult,juvenile='adult','juvenile'
   # age_choices=((adult,"Adult"),(juvenile, "Juvenile"),)
   # Age=models.CharField(help_text='Age',max_length=200,choices=age_choices)
    
  #  gray,cinnamon,black='gray','cinnamon','black'
   # fur_choices=((gray,"Gray,"),(cinnamon, "Cinnamon"),(black,"Black"),)
   # Primary_fur_color=models.CharField(help_text='Primary Fur Color',max_length=200,choices=fur_choices)
    
  #  ground_plane,above_ground="ground plane","above ground"
  #  location_choices=((ground_plane,"Ground Plane",),(above_ground,"Above Ground"),)    
  #  Location=models.CharField(help_text='Location',max_length=200,choices=location_choices)
    
   # Specific_location=models.CharField(help_text='Specific Location',max_length=200,)
    
   # Running=models.NullBooleanField(help_text='Running')
    
  #  Chasing=models.NullBooleanField(help_text='Chasing')
    
   # Climbing=models.NullBooleanField(help_text='Climbing')
    
   # Eating=models.NullBooleanField(help_text='Eating')
    
   # Foraging=models.NullBooleanField(help_text='Foraging')
    
   # Other_Activities=models.CharField(help_text='Other Activities',max_length=200,)
    
   # Kuks=models.NullBooleanField(help_text='Kuks')
    
   # Quaas=models.NullBooleanField(help_text='Quaas')
    
   # Moans=models.NullBooleanField(help_text='Moans')
    
   # Tail_flags=models.NullBooleanField(help_text='Tail_flags')
    
   # Tail_twitches=models.NullBooleanField(help_text='Tail twitches')
    
   # Approaches=models.NullBooleanField(help_text='Approaches')
    
   # Indifferent=models.NullBooleanField(help_text='Indifferent')
    
   # Runs_from=models.NullBooleanField(help_text='Runs from')
    
    def __str__(self):
        return self.Unique_Squirrel_ID
