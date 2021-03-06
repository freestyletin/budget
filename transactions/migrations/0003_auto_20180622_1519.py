# Generated by Django 2.2.dev20180619125833 on 2018-06-22 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20180621_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transaction_as_address_set', to='contacts.Address', verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='transactiondetail',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactiondetail_as_transaction_set', to='transactions.Transaction', verbose_name='transaction'),
        ),
    ]
