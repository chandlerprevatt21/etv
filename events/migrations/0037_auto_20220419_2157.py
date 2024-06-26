# Generated by Django 3.2.10 on 2022-04-20 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0036_event_checkout_video_html'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['title'], 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='singleticket',
            options={'ordering': ['-created'], 'verbose_name': 'Ticket', 'verbose_name_plural': 'Tickets'},
        ),
        migrations.AlterModelOptions(
            name='tickettype',
            options={'ordering': ['event', 'price'], 'verbose_name': 'Ticket Type', 'verbose_name_plural': 'Ticket Types'},
        ),
        migrations.AddField(
            model_name='singleticket',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=270, null=True),
        ),
    ]
