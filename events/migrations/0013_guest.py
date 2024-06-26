# Generated by Django 3.2.10 on 2021-12-13 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20211212_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=270, null=True)),
                ('last_name', models.CharField(blank=True, max_length=270, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
