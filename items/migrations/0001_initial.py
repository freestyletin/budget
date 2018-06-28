# Generated by Django 2.2.dev20180619125833 on 2018-06-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenericItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Item')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upc', models.CharField(max_length=255, verbose_name='UPC Code')),
                ('model_number', models.CharField(max_length=255, verbose_name='Model/Item Number')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('milliliters_custom', models.DecimalField(decimal_places=5, max_digits=10, verbose_name='Custom Milliliters')),
                ('unit_factor_custom', models.DecimalField(decimal_places=5, max_digits=10, verbose_name='Custom Unit Factor')),
            ],
        ),
    ]