# Generated by Django 3.2.10 on 2022-05-19 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_alter_disbursement_disbursement_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BraintreeTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('braintree_id', models.CharField(max_length=50)),
            ],
        ),
    ]
