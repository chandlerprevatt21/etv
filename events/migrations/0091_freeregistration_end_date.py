# Generated by Django 4.1.2 on 2024-01-26 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0090_freeregistration_affiliation'),
    ]

    operations = [
        migrations.AddField(
            model_name='freeregistration',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
