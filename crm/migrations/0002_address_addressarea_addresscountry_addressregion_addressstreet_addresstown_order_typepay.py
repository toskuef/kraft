# Generated by Django 3.2.12 on 2022-03-31 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='назавние области')),
            ],
            options={
                'verbose_name': 'область',
                'verbose_name_plural': 'области',
            },
        ),
        migrations.CreateModel(
            name='AddressCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='назавние страны')),
            ],
            options={
                'verbose_name': 'страна',
                'verbose_name_plural': 'страны',
            },
        ),
        migrations.CreateModel(
            name='AddressRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название района')),
            ],
            options={
                'verbose_name': 'район',
                'verbose_name_plural': 'районы',
            },
        ),
        migrations.CreateModel(
            name='AddressStreet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название улицы')),
            ],
            options={
                'verbose_name': 'улица',
                'verbose_name_plural': 'улицы',
            },
        ),
        migrations.CreateModel(
            name='AddressTown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название города')),
            ],
            options={
                'verbose_name': 'город',
                'verbose_name_plural': 'города',
            },
        ),
        migrations.CreateModel(
            name='TypePay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_pay', models.CharField(max_length=150, verbose_name='тип оплаты')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='сумма заказа')),
                ('pre_pay', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='предоплата')),
                ('second_pay', models.DecimalField(blank=True, decimal_places=2, max_digits=20, verbose_name='второй взнос')),
                ('date_create', models.DateField(auto_now_add=True)),
                ('date_done', models.DateField()),
                ('date_pre_pay', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='crm.customer', verbose_name='клиент')),
                ('pre_pay_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pre_pay_types', to='crm.typepay', verbose_name='тип предоплаты')),
                ('second_pay_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='second_pay_types', to='crm.typepay', verbose_name='тип второго платежа')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_house', models.IntegerField(blank=True, verbose_name='номер дома')),
                ('num_housing', models.IntegerField(blank=True, verbose_name='номер корпуса')),
                ('num_door', models.IntegerField(blank=True, verbose_name='номер подъезда')),
                ('num_level', models.IntegerField(blank=True, verbose_name='номер этажа')),
                ('num_flat', models.IntegerField(blank=True, verbose_name='номер квартиры')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to='crm.addressarea', verbose_name='область')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to='crm.addresscountry', verbose_name='страна')),
                ('customer', models.ManyToManyField(blank=True, related_name='addresses', to='crm.Customer', verbose_name='клиенты')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to='crm.addressregion', verbose_name='район')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to='crm.addressstreet', verbose_name='улица')),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to='crm.addresstown', verbose_name='город')),
            ],
            options={
                'verbose_name': 'адрес',
                'verbose_name_plural': 'адреса',
            },
        ),
    ]
