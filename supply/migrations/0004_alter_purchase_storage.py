# Generated by Django 3.2.12 on 2022-05-14 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0003_purchase_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchase', to='supply.storage', verbose_name='склад'),
        ),
    ]