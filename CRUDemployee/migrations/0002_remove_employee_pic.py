# Generated by Django 3.1.2 on 2020-10-31 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDemployee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='pic',
        ),
    ]