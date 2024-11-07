# Generated by Django 5.1.1 on 2024-11-07 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0007_alter_category_time'),
        ('app_user', '0007_user_date_joined_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='room',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='app_admin.room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='app_user.user'),
        ),
    ]
