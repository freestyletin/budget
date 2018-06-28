# Generated by Django 2.2.dev20180619125833 on 2018-06-21 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20180620_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address_as_contact_set', to='contacts.Contact'),
        ),
    ]
