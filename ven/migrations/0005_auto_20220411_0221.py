# Generated by Django 3.2.10 on 2022-04-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ven', '0004_auto_20220324_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='familynomination',
            name='counselor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='nomination',
            name='counselor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
