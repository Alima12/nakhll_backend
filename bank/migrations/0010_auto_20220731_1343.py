# Generated by Django 3.2.14 on 2022-07-31 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0009_accountrequest_cashable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounttransaction',
            name='cashable',
        ),
        migrations.AddField(
            model_name='accounttransaction',
            name='cashable_value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
