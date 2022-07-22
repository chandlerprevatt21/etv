# Generated by Django 4.0.5 on 2022-06-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0045_alter_galleryitem_options_galleryitem_pre_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='FullGalleryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=270)),
                ('artist', models.CharField(max_length=270)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('width', models.CharField(blank=True, max_length=20)),
                ('height', models.CharField(blank=True, max_length=20)),
                ('sold', models.BooleanField(default=False)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('pre_sale', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Juneteenth Art Show Item',
                'verbose_name_plural': 'Juneteenth Art Show Items',
                'ordering': ['artist', 'price'],
            },
        ),
        migrations.AlterModelOptions(
            name='galleryitem',
            options={'ordering': ['artist', 'price'], 'verbose_name': 'Juneteenth Pre-Sale Art Show Item', 'verbose_name_plural': 'Juneteenth Pre-Sale Art Show Items'},
        ),
    ]