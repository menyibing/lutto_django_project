# Generated by Django 2.1.1 on 2018-10-19 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181019_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='kucun',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
