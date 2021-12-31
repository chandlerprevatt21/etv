# Generated by Django 3.2.10 on 2021-12-22 09:35

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vbpscraped',
            options={'verbose_name': 'Business', 'verbose_name_plural': 'Businesses'},
        ),
        migrations.AddField(
            model_name='vbpscraped',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='vbpscraped',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='vbpscraped',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='vbpscraped',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='vbpscraped',
            name='subcategory',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='vbpscraped',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
