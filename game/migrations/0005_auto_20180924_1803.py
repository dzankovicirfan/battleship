# Generated by Django 2.1.1 on 2018-09-24 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20180924_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='ship',
            field=models.SmallIntegerField(choices=[(1, 'Destroyer'), (2, 'Submarine'), (3, 'Cruiser'), (4, 'Battleship'), (5, 'Carrier')]),
        ),
    ]
