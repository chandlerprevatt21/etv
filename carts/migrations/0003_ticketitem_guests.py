# Generated by Django 3.2.10 on 2021-12-14 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20211212_2304'),
        ('carts', '0002_ticketcart_ticketitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketitem',
            name='guests',
            field=models.ManyToManyField(blank=True, to='events.Guest'),
        ),
    ]