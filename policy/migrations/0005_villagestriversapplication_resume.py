# Generated by Django 4.1.2 on 2023-10-02 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0004_villagestriversapplication_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='villagestriversapplication',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
