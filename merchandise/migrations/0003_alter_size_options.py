# Generated by Django 3.2.10 on 2022-03-24 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0002_size_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': ['order']},
        ),
    ]
