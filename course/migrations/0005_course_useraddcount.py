# Generated by Django 2.1.1 on 2018-10-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20181023_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='useraddcount',
            field=models.IntegerField(default=0),
        ),
    ]
