# Generated by Django 2.2.6 on 2021-01-10 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20210105_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_created=True)),
                ('mobile_number', models.CharField(max_length=15, verbose_name='')),
                ('client_ip', models.GenericIPAddressField(verbose_name='')),
                ('template', models.CharField(max_length=50, verbose_name='')),
                ('token', models.CharField(max_length=10, verbose_name='')),
                ('type', models.CharField(choices=[('sms', 'sms'), ('sms', 'call')], default='sms', max_length=4, verbose_name='')),
                ('block_message', models.CharField(blank=True, max_length=127, null=True, verbose_name='')),
            ],
        ),
    ]
