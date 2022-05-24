# Generated by Django 3.1.6 on 2022-05-01 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nakhll_market', '0146_auto_20220501_1906'),
        ('invoice', '0030_auto_20220501_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='invoice.invoice', verbose_name='فاکتور'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_items', to='nakhll_market.product'),
        ),
    ]