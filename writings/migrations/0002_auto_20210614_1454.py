# Generated by Django 2.2.20 on 2021-06-14 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='writings',
            old_name='summary',
            new_name='writing_text',
        ),
        migrations.RemoveField(
            model_name='writings',
            name='content',
        ),
    ]
