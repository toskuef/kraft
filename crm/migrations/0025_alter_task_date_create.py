# Generated by Django 3.2.12 on 2022-06-05 23:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0024_alter_task_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_create',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]