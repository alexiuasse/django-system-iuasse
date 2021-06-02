# Generated by Django 3.2.3 on 2021-06-02 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_contract_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='name',
            field=models.CharField(default='friendly name', help_text='A friendly name to easy renember.', max_length=32, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]
