# Generated by Django 2.2.24 on 2021-10-09 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hindiblog', '0005_hindiblog_likes_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hindiblog',
            old_name='likes_total',
            new_name='vote',
        ),
    ]
