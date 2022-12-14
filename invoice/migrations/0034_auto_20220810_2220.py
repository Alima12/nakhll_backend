# Generated by Django 3.2.14 on 2022-08-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0033_auto_20220726_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='coin_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12, verbose_name='مبلغ سکه های پرداخت شده'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='coins_amount',
            field=models.IntegerField(default=0, verbose_name='coins amount'),
        ),
    ]
