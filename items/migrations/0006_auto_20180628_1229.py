# Generated by Django 2.2.dev20180619125833 on 2018-06-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20180624_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='qty_test',
        ),
        migrations.AlterField(
            model_name='item',
            name='milliliters_custom',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, verbose_name='Custom Milliliters'),
        ),
        migrations.AlterField(
            model_name='item',
            name='unit_factor_custom',
            field=models.DecimalField(decimal_places=5, default=1, max_digits=10, verbose_name='Custom Unit Factor'),
        ),
    ]
