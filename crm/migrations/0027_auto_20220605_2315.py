# Generated by Django 3.2.12 on 2022-06-05 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0026_auto_20220605_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_task', models.CharField(max_length=150, verbose_name='тип задачи')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='type_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='crm.typetask', verbose_name='тип задачи'),
        ),
    ]