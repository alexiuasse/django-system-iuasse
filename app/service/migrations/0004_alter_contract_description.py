# Generated by Django 3.2.3 on 2021-05-31 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_contract_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
    ]
