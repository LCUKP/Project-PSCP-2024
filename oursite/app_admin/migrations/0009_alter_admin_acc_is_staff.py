# Generated by Django 5.1.1 on 2024-11-08 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0008_admin_acc_date_joined_admin_acc_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_acc',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
