# Generated by Django 3.2.15 on 2023-01-25 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_kyc_walletaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kyc',
            old_name='GSTnumber',
            new_name='PANnumber',
        ),
    ]
