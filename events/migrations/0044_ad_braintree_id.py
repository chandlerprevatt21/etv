# Generated by Django 3.2.10 on 2022-05-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0043_auto_20220506_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=270),
        ),
    ]