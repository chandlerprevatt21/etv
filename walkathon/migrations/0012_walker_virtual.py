# Generated by Django 4.1.2 on 2023-04-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walkathon', '0011_orgdonation_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='walker',
            name='virtual',
            field=models.BooleanField(default=False),
        ),
    ]
