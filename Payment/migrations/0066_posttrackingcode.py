# Generated by Django 3.1.6 on 2021-07-17 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0065_delete_dashboardbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTrackingCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=24, verbose_name='بارکد')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد بارکد')),
                ('post_price', models.DecimalField(decimal_places=0, default='0', max_digits=8, max_length=15, verbose_name='هزینه ارسال')),
                ('post_type', models.CharField(choices=[('irpost', 'شرکت پست جمهوری اسلامی ایران'), ('tipax', 'تیپاکس')], default='irpost', max_length=6, verbose_name='نوع پست')),
                ('send_type', models.CharField(choices=[('in_c', 'درون شهری'), ('norm', 'پست معمولی'), ('pad', 'پس کرایه')], default='norm', max_length=4, verbose_name='وضعیت ارسال')),
                ('factor_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barcodes', to='Payment.factorpost', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'بارکد پستی',
                'verbose_name_plural': 'بارکدهای پستی',
            },
        ),
    ]