# Generated by Django 3.2.10 on 2022-03-31 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0006_alter_donor_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
    ]
