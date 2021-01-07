# Generated by Django 3.1.4 on 2021-01-06 17:55

from django.db import migrations


def seed(apps, schema_editor):
    Lego = apps.get_model('legos', 'Lego')

    Lego(name='Mini Sith Infiltrator', set_number=4493, piece_count=55, source='Episode I', release_year=2004,
         image_url='https://images.brickset.com/sets/images/4493-1.jpg?200310020124', minifigures=['None'], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()
    # Lego(name='', set_number=, piece_count=, source='', release_year=,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()

def fallow(apps, schema_editor):
    Lego = apps.get_model('legos', 'Lego')
    Lego.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('legos', '0004_auto_20201217_1752'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]