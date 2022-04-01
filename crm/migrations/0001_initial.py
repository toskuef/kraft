# Generated by Django 3.2.12 on 2022-03-30 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SourceCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=15, verbose_name='Источник')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('family_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to='crm.sourcecustomer', verbose_name='Источник')),
            ],
        ),
    ]