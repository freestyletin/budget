# Generated by Django 2.2.dev20180619125833 on 2018-06-22 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20180622_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericitem',
            name='base_unit_custom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genericitem_as_base_unit_custom_set', to='units.Unit', verbose_name='custom base unit'),
        ),
        migrations.AlterField(
            model_name='item',
            name='base_unit_custom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_as_base_unit_custom_set', to='units.Unit', verbose_name='custom base unit'),
        ),
        migrations.AlterField(
            model_name='item',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_as_unit_set', to='units.Unit', verbose_name='unit'),
        ),
    ]
