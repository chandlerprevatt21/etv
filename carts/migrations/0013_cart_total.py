# Generated by Django 4.1.2 on 2023-11-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0012_alter_ticketad_cart_alter_ticketdonation_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
