# Generated by Django 3.2.3 on 2021-06-01 14:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20210531_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
    ]
