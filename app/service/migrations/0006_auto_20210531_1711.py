# Generated by Django 3.2.3 on 2021-05-31 20:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_domain_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
        migrations.AddField(
            model_name='domain',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
        migrations.AddField(
            model_name='webservice',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
    ]