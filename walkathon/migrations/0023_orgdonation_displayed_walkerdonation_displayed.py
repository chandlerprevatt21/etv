# Generated by Django 4.1.2 on 2023-11-12 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walkathon', '0022_organization_created_organization_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgdonation',
            name='displayed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='walkerdonation',
            name='displayed',
            field=models.BooleanField(default=False),
        ),
    ]
