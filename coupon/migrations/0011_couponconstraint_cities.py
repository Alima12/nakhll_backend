# Generated by Django 3.1.6 on 2021-11-23 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0132_auto_20211108_1121'),
        ('coupon', '0010_auto_20211023_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponconstraint',
            name='cities',
            field=models.ManyToManyField(blank=True, related_name='coupons', to='nakhll_market.City', verbose_name='شهرها'),
        ),
    ]