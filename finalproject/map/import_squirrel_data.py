from map.models import squirrels

import csv
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                squirrels = squirrels.objects.create(
                    Longitude=row[0]
                    Latitude=row[1]
                )               
