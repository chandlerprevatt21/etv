# Generated by Django 3.2.8 on 2021-11-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0003_donor_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='category',
            field=models.CharField(blank=True, max_length=270, null=True),
        ),
    ]
