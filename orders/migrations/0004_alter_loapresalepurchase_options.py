# Generated by Django 3.2.10 on 2022-05-07 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20220504_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loapresalepurchase',
            options={'ordering': ['-timestamp', '-updated'], 'verbose_name': 'Juneteenth Pre-Sale Order', 'verbose_name_plural': 'Juneteenth Pre-Sale Orders'},
        ),
    ]
