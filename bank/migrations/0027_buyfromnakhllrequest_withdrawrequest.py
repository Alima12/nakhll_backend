# Generated by Django 3.2.14 on 2022-08-18 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0026_depositrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyFromNakhllRequest',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('bank.accountrequest',),
        ),
        migrations.CreateModel(
            name='WithdrawRequest',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('bank.accountrequest',),
        ),
    ]
