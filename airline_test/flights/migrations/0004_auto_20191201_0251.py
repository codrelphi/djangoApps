# Generated by Django 2.2.7 on 2019-12-01 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_auto_20191201_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(max_length=3),
        ),
    ]
