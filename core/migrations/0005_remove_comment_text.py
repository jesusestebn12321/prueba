# Generated by Django 3.0.8 on 2021-10-12 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211012_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
    ]
