# Generated by Django 3.2.5 on 2023-01-17 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geography', '0001_initial'),
        ('fleet', '0002_auto_20211109_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stopplace', to='geography.place')),
            ],
        ),
        migrations.CreateModel(
            name='BusShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='busshift', to='fleet.bus')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shiftdriver', to='fleet.driver')),
                ('stops', models.ManyToManyField(related_name='shiftstops', to='trips.BusStop')),
            ],
        ),
    ]
