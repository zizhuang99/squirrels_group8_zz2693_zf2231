# Generated by Django 2.2.7 on 2019-11-24 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='squirrels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Longitude', models.DecimalField(decimal_places=2, help_text='Longitude', max_digits=20, max_length=200)),
                ('Latitude', models.DecimalField(decimal_places=2, help_text='Latitude', max_digits=20, max_length=200)),
                ('Unique_Squirrel_ID', models.CharField(help_text='Unique Squirrel ID', max_length=200)),
                ('Shift', models.CharField(choices=[('AM', 'am'), ('PM', 'pm')], help_text='Shift', max_length=200)),
                ('Date', models.DateField(help_text='Date', max_length=200)),
                ('Age', models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile')], help_text='Age', max_length=200)),
                ('Primary_fur_color', models.CharField(choices=[('gray', 'Gray,'), ('cinnamon', 'Cinnamon'), ('black', 'Black')], help_text='Primary Fur Color', max_length=200)),
                ('Location', models.CharField(choices=[('ground plane', 'Ground Plane'), ('above ground', 'Above Ground')], help_text='Location', max_length=200)),
                ('Specific_location', models.CharField(help_text='Specific Location', max_length=200)),
                ('Running', models.NullBooleanField(help_text='Running')),
                ('Chasing', models.NullBooleanField(help_text='Chasing')),
                ('Climbing', models.NullBooleanField(help_text='Climbing')),
                ('Eating', models.NullBooleanField(help_text='Eating')),
                ('Foraging', models.NullBooleanField(help_text='Foraging')),
                ('Other_Activities', models.CharField(help_text='Other Activities', max_length=200)),
                ('Kuks', models.NullBooleanField(help_text='Kuks')),
                ('Quaas', models.NullBooleanField(help_text='Quaas')),
                ('Moans', models.NullBooleanField(help_text='Moans')),
                ('Tail_flags', models.NullBooleanField(help_text='Tail_flags')),
                ('Tail_twitches', models.NullBooleanField(help_text='Tail twitches')),
                ('Approaches', models.NullBooleanField(help_text='Approaches')),
                ('Indifferent', models.NullBooleanField(help_text='Indifferent')),
                ('Runs_from', models.NullBooleanField(help_text='Runs from')),
            ],
        ),
    ]
