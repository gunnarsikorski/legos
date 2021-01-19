# Generated by Django 3.1.4 on 2021-01-19 20:05

from django.db import migrations


def seed(apps, schema_editor):
    Lego = apps.get_model('legos', 'Lego')

    Lego(name='The Phantom', set_number=75048, piece_count=234, source='Rebels', release_year=2014,
         image_url='https://images.brickset.com/sets/images/75048-1.jpg?201402141049', minifigures=['Ezra Bridger', 'Chopper'], set_series='Star Wars').save()
    Lego(name='Snowspeeder', set_number=75049, piece_count=278, source='Episode V', release_year=2014,
         image_url='https://images.brickset.com/sets/images/75049-1.jpg?201402170929', minifigures=['Dak Ralter', 'Luke Skywalker', 'Snowtrooper'], set_series='Star Wars').save()
    Lego(name='B-Wing', set_number=75050, piece_count=448, source='Episode VI', release_year=2014,
         image_url='https://images.brickset.com/sets/images/75050-1.jpg?201402170929', minifigures=['General Airen Cracken', 'Gray Squadron Pilot', 'Ten Numb'], set_series='Star Wars').save()
    Lego(name='Jedi Scout Fighter', set_number=75051, piece_count=490, source='Expanded Universe', release_year=2014,
         image_url='https://images.brickset.com/sets/images/75051-1.jpg?201402170929', minifigures=['Jek-14', 'Astromech Droid', 'Ithorian Jedi Master', 'RA-7 Protocol Droid'], set_series='Star Wars').save()
    Lego(name='The Ghost', set_number=75053, piece_count=929, source='', release_year=2014,
         image_url='https://images.brickset.com/sets/images/75053-1.jpg?201402141049', minifigures=['Hera Syndulla', 'Kanan Jarrus', 'Zeb Orrelios', 'Stormtrooper'], set_series='Star Wars').save()
    Lego(name='Advent Calendar', set_number=75056, piece_count=274, source='Expanded Universe', release_year=2014,
         image_url='https://images.brickset.com/sets/images/75056-1.jpg?201402170929', minifigures=['Clone Trooper (Santa)', 'Festive Astromech', 'General Rieekan', 'Luke Skywalker (Tatooine)', 'Darth Vader (Santa)', 'Snowspeeder Pilot', 'Snowtrooper', 'Super Battle Droid', 'TIE Fighter Pilot'], set_series='Star Wars').save()
    Lego(name='MTT', set_number=75058, piece_count=954, source='Episode I', release_year=2014,
         image_url='https://images.brickset.com/sets/images/75058-1.jpg?201405270447', minifigures=['Obi-Wan Kenobi', 'Qui-Gon Jinn', 'Battle Droid Pilot', 'Battle Droid (7x)', 'Naboo Security Guard', 'PK-4 Droid'], set_series='Star Wars').save()
    Lego(name='Darth Revan', set_number=5002123, piece_count=7, source='Expanded Universe', release_year=2014,
         image_url='https://images.brickset.com/sets/images/5002123-1.jpg?201605160806', minifigures=['Darth Revan'], set_series='Star Wars').save()
    Lego(name='TC-4', set_number=5002122, piece_count=3, source='Expanded Universe', release_year=2014,
         image_url='https://images.brickset.com/sets/images/5002122-1.jpg?201401040948', minifigures=['TC-4'], set_series='Star Wars').save()
         
    # Lego(name='', set_number=, piece_count=, source='', release_year=2014,
    #      image_url='', minifigures=['', '', ''], set_series='Star Wars').save()

def fallow(apps, schema_editor):
    Lego = apps.get_model('legos', 'Lego')
    Lego.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('legos', '0012_auto_20210118_1850'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]