# Generated by Django 2.2.7 on 2019-12-01 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_auto_20191201_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]
