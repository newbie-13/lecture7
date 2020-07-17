# Generated by Django 3.0.8 on 2020-07-16 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_auto_20200716_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passenger', to='flights.Flight')),
            ],
        ),
    ]
