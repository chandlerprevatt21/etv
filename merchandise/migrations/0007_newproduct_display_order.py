# Generated by Django 4.1.2 on 2023-11-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0006_alter_newproduct_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='newproduct',
            name='display_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
