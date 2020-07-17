# Generated by Django 3.0.8 on 2020-07-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight'),
        ),
    ]
