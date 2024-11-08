# Generated by Django 5.1.1 on 2024-11-08 05:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0007_alter_category_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_acc',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='admin_acc',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='admin_acc',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='admin_acc',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='admin_acc',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]