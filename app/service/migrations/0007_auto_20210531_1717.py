# Generated by Django 3.2.3 on 2021-05-31 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20210531_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='date',
        ),
        migrations.RemoveField(
            model_name='domain',
            name='date',
        ),
        migrations.RemoveField(
            model_name='webservice',
            name='date',
        ),
    ]