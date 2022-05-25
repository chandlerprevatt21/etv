# Generated by Django 3.2.10 on 2022-05-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0012_braintreetransaction_payment_method'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='braintreetransaction',
            options={'ordering': ['-amount']},
        ),
        migrations.AlterModelOptions(
            name='disbursement',
            options={'ordering': ['-disbursement_date']},
        ),
        migrations.AddField(
            model_name='braintreetransaction',
            name='url',
            field=models.CharField(max_length=270, null=True),
        ),
    ]