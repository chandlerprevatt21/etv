# Generated by Django 3.2.10 on 2022-03-05 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vbp', '0028_rename_vbp_ind_vbp_ndi'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vbp_in',
            options={'verbose_name': 'Indiana Listing', 'verbose_name_plural': 'Indiana Listings'},
        ),
        migrations.DeleteModel(
            name='vbp_ndi',
        ),
    ]
