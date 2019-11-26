#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finalproject.settings')
    try:
        from django.core.management import execute_from_command_line,BaseCommand
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

#def import_squirrel_data(path):
 #   with open(path, 'rt') as f:
  #      reader = csv.reader(f, dialect='excel')
   #     for row in reader:
    #        squirrels.objects.create(
     #       Longitude=row[0],
      #      Latitude=row[1]
     #       )
if __name__ == '__main__':
    main()
    #import_squirrel_data(path)
