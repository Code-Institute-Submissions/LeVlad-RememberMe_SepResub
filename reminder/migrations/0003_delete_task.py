# Generated by Django 3.2.13 on 2022-09-13 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_rename_item_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
