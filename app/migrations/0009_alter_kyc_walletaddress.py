# Generated by Django 3.2.15 on 2023-01-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20230125_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='WalletAddress',
            field=models.CharField(default='', max_length=200),
        ),
    ]
