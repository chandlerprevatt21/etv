# Generated by Django 3.2.6 on 2021-09-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfchallenge', '0010_auto_20210906_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='everyfriday_transaction',
            name='receipt',
        ),
        migrations.AddField(
            model_name='everyfriday_transaction',
            name='receipt_aws',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
