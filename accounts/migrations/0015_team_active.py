# Generated by Django 3.2.8 on 2021-12-01 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20211130_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]