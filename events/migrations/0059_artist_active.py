# Generated by Django 3.2.10 on 2022-10-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0058_fullgalleryitem_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
