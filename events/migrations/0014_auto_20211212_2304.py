# Generated by Django 3.2.10 on 2021-12-13 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_guest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singleticket',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='singleticket',
            name='last_name',
        ),
        migrations.AddField(
            model_name='singleticket',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.guest'),
        ),
    ]