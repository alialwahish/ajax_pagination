# Generated by Django 2.0.5 on 2018-08-05 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxP', '0004_auto_20180805_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='registered_datetime',
            field=models.DateField(),
        ),
    ]
