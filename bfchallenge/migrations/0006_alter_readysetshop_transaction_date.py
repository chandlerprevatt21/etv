# Generated by Django 3.2.6 on 2021-08-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfchallenge', '0005_readysetshop_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readysetshop_transaction',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
