# Generated by Django 4.2.1 on 2023-06-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_comments_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='song',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='songs',
        ),
        migrations.AddField(
            model_name='song',
            name='genres',
            field=models.ManyToManyField(related_name='songs', to='main_app.genre'),
        ),
    ]
