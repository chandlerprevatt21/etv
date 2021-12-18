# Generated by Django 3.2.8 on 2021-11-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='company',
            field=models.CharField(blank=True, max_length=270, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]