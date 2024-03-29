# Generated by Django 2.2.6 on 2019-11-24 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20191125_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='from_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.City'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='to_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city', to='home.City'),
        ),
    ]
