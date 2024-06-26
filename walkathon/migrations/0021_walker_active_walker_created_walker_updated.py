# Generated by Django 4.1.2 on 2023-11-12 23:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('walkathon', '0020_organization_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='walker',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='walker',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='walker',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
