# Generated by Django 3.2.10 on 2022-03-25 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
        ('events', '0027_tickettype_price_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=270, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sale_description', models.CharField(blank=True, max_length=270, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event')),
            ],
            options={
                'verbose_name': 'Ad Type',
                'verbose_name_plural': 'Ad Types',
            },
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.ImageField(blank=True, null=True, upload_to='')),
                ('ad_id', models.CharField(blank=True, max_length=270)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.billingprofile')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.tickettype')),
            ],
            options={
                'verbose_name': 'Ad',
                'verbose_name_plural': 'Ads',
            },
        ),
    ]
