# Generated by Django 3.2.10 on 2022-04-05 20:56

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0035_auto_20220402_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='checkout_video_html',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
