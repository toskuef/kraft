# Generated by Django 3.2.12 on 2022-05-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0004_alter_purchase_storage'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='is_order',
            field=models.BooleanField(default=False),
        ),
    ]