# Generated by Django 3.1.5 on 2021-01-19 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_game', '0022_auto_20210119_0126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='avg_score',
            new_name='avg',
        ),
    ]