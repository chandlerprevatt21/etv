# Generated by Django 3.2.10 on 2022-04-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_dashboardmodel_view_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardmodel',
            name='grouping',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
