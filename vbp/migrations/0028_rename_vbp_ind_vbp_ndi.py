# Generated by Django 3.2.10 on 2022-03-04 21:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0015_team_active'),
        ('vbp', '0027_vbp_book_featured'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='vbp_ind',
            new_name='vbp_ndi',
        ),
    ]
