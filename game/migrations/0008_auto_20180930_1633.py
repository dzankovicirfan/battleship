# Generated by Django 2.1.1 on 2018-09-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_shipposition_horizontal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='ship',
            field=models.SmallIntegerField(choices=[(1, 'Destroyer'), (2, 'Submarine'), (3, 'Destroyer'), (4, 'Battleship'), (5, 'Carrier')], default=1),
        ),
    ]
