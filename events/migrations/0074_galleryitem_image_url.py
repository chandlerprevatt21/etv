# Generated by Django 4.1.2 on 2023-07-21 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0073_event_checkout_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryitem',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]