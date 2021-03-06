# Generated by Django 2.1.1 on 2018-09-25 16:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20180924_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('y', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shippositions', to='game.Ship')),
            ],
            options={
                'verbose_name': 'shippostion',
                'verbose_name_plural': 'shippostions',
            },
        ),
    ]
