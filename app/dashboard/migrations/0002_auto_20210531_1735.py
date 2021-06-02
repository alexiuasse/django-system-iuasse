# Generated by Django 3.2.3 on 2021-05-31 20:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardsettings',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboardsettings',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]