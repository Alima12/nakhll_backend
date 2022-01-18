# Generated by Django 3.1.6 on 2022-01-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0019_shoplogisticunit_logo_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoplogisticunitcalculationmetric',
            name='price_per_extra_kilogram',
            field=models.FloatField(default=0, verbose_name='قیمت به ازای هر کیلو اضافه (ریال)'),
        ),
        migrations.AlterField(
            model_name='shoplogisticunitcalculationmetric',
            name='price_per_kilogram',
            field=models.FloatField(default=0, verbose_name='قیمت به ازای هر کیلو (ریال)'),
        ),
    ]
