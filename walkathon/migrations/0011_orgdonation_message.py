# Generated by Django 4.1.2 on 2023-04-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walkathon', '0010_alter_walker_options_walkerdonation_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgdonation',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
