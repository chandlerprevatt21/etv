# Generated by Django 3.2.10 on 2021-12-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='addon',
            name='options',
            field=models.ManyToManyField(blank=True, to='events.Option'),
        ),
    ]
