# Generated by Django 3.0.8 on 2020-12-28 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0004_auto_20201228_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtuber',
            old_name='decription',
            new_name='description',
        ),
    ]
