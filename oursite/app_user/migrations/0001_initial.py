# Generated by Django 5.1.1 on 2024-10-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('userid', models.AutoField(auto_created=True,primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
