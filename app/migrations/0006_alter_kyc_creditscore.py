# Generated by Django 3.2.15 on 2023-01-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_kyc_walletaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='CreditScore',
            field=models.CharField(default='', max_length=5),
        ),
    ]