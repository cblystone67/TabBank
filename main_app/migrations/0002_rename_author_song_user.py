# Generated by Django 4.2.1 on 2023-06-08 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='author',
            new_name='user',
        ),
    ]