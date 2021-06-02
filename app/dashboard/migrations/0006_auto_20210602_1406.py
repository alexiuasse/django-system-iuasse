# Generated by Django 3.2.3 on 2021-06-02 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210602_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardsettings',
            name='month_earn_metric',
        ),
        migrations.RemoveField(
            model_name='dashboardsettings',
            name='year_earn_metric',
        ),
        migrations.AddField(
            model_name='dashboardsettings',
            name='month_earn_goal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Month Earn Goal'),
        ),
        migrations.AddField(
            model_name='dashboardsettings',
            name='year_earn_goal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Year Earn Goal'),
        ),
    ]
