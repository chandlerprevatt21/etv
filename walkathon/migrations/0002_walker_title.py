# Generated by Django 4.1.2 on 2023-04-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walkathon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='walker',
            name='title',
            field=models.CharField(default='ayo wilson', max_length=270),
            preserve_default=False,
        ),
    ]
