# Generated by Django 2.2.dev20180619125833 on 2018-06-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0002_unit_subunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Unit'),
        ),
    ]
