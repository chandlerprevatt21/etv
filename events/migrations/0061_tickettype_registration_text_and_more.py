# Generated by Django 4.1.2 on 2023-01-07 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0060_alter_artist_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='registration_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tickettype',
            name='registration_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]