# Generated by Django 3.2.3 on 2021-05-23 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='contracts', verbose_name='Attachment'),
        ),
    ]