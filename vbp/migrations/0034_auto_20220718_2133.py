# Generated by Django 3.2.10 on 2022-07-19 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vbp', '0033_mv_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='mv_private',
            name='owner_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='mv_private',
            name='owner_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
