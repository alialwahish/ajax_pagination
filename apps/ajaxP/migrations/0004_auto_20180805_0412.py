# Generated by Django 2.0.5 on 2018-08-05 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxP', '0003_auto_20180805_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='registered_datetime',
            field=models.CharField(max_length=255),
        ),
    ]
