# Generated by Django 3.2.6 on 2021-09-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vbp', '0009_auto_20210901_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vbp_book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
