# Generated by Django 3.2.10 on 2022-04-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ven', '0007_auto_20220411_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomination',
            name='facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nomination',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nomination',
            name='twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
