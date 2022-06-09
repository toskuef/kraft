# Generated by Django 3.2.12 on 2022-05-30 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20220530_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='status_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='crm.statusorder', verbose_name='статус заказа'),
        ),
    ]
