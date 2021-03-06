# Generated by Django 3.2.8 on 2021-11-13 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=270, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='donation_submission',
            name='source',
            field=models.CharField(blank=True, default='Website', max_length=270, null=True),
        ),
        migrations.CreateModel(
            name='donation_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=270, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('tags', models.ManyToManyField(blank=True, to='donations.tag')),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='donations.donation_event'),
        ),
    ]
