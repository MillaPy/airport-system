# Generated by Django 2.2.6 on 2019-11-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191124_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_duration',
            field=models.IntegerField(),
        ),
    ]
