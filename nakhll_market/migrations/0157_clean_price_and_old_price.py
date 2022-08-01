# Generated by Django 3.2.14 on 2022-07-24 10:21

from django.db import migrations
from django.db.models import Q, F


def modify_product_price(apps, schema_editor):
    Product = apps.get_model("nakhll_market", "Product")
    # products with price = 0
    Product.objects.filter(Price=0).update(Price=10000, OldPrice=0)
    # products with OldPrice != 0 and OldPrice < Price
    Product.objects.filter(
        Q(OldPrice__gt=0) and
        Q(OldPrice__lte=F("Price"))).update(
        OldPrice=0)


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0156_auto_20220723_1318'),
    ]

    operations = [
        migrations.RunPython(modify_product_price, migrations.RunPython.noop),
    ]
