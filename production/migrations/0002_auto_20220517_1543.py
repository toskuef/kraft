# Generated by Django 3.2.12 on 2022-05-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productorder',
            name='is_specification_done',
            field=models.BooleanField(default=True),
        ),
    ]
