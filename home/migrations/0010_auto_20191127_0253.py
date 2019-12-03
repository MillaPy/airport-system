# Generated by Django 2.2.6 on 2019-11-26 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191127_0220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='flight_business_places',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='flight_econom_places',
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_econom_places', models.IntegerField(default=60)),
                ('flight_business_places', models.IntegerField(default=10)),
                ('fligth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Flight')),
                ('fligth_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Day')),
            ],
        ),
    ]