# Generated by Django 2.1.1 on 2018-09-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20180924_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='ship',
            field=models.CharField(choices=[(1, 'Destroyer'), (2, 'Submarine'), (3, 'Cruiser'), (4, 'Battleship'), (5, 'Carrier')], max_length=1),
        ),
    ]