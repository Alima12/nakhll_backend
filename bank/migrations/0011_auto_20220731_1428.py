# Generated by Django 3.2.14 on 2022-07-31 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0010_auto_20220731_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountrequest',
            name='cashable',
        ),
        migrations.AddField(
            model_name='accountrequest',
            name='cashable_value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
