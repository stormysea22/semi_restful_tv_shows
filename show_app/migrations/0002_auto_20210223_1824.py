# Generated by Django 2.2.4 on 2021-02-23 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='Network',
            new_name='network',
        ),
    ]
