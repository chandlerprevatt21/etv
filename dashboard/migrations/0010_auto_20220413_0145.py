# Generated by Django 3.2.10 on 2022-04-13 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_dashboardmodel_grouping'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardmodel',
            name='model_name_verbose',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='model_name_verbose_plural',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
