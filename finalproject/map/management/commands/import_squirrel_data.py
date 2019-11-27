from map.models import squirrels

import csv
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('positionArg')

    def handle(self,*args,**kargs):
        path=kargs['positionArg']
        with open(path, 'rt') as f:
            reader = csv.DictReader(f, dialect='excel')
            for row in reader:
                squirrels.objects.create(
                    Unique_Squirrel_ID=row['unique_squirrel_id'],
                    Longitude=row['x'],
                    Latitude=row['y'],
                    Shift=row['shift'],
                    Date=row['date'][4:]+'-'+row['date'][:2]+'-'+row['date'][2:4],
                    Age=row['age'],
                    Primary_fur_color=row['primary_fur_color'],
                    Location=row['location'],
                    Specific_location=row['specific_location'],
                    Running=row['running'].capitalize(),
                    Chasing=row['chasing'].capitalize(),
                    Climbing=row['climbing'].capitalize(),
                    Eating=row['eating'].capitalize(),
                    Foraging=row['foraging'].capitalize(),
                    Other_Activities=row['other_activities'],
                    Kuks=row['kuks'].capitalize(),
                    Quaas=row['quaas'].capitalize(),
                    Moans=row['moans'].capitalize(),
                    Tail_flags=row['tail_flags'].capitalize(),
                    Tail_twitches=row['tail_twitches'].capitalize(),
                    Approaches=row['approaches'].capitalize(),
                    Indifferent=row['indifferent'].capitalize(),
                    Runs_from=row['runs_from'].capitalize()

                    
                    )
