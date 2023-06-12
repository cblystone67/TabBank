# Generated by Django 4.2.1 on 2023-06-12 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_author_song_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Created Date')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('style', models.CharField(choices=[('ALT', 'Alternative'), ('BLU', 'Blues'), ('CLC', 'Classical'), ('CNY', 'Country'), ('EDM', 'Electronic Dance Music'), ('HIP', 'Hip Hop'), ('JAZ', 'Jazz'), ('MTL', 'Metal'), ('POP', 'Pop'), ('RNB', 'Rhythm and Blues'), ('RCK', 'Rock'), ('REG', 'Reggae'), ('IND', 'Indie'), ('FOL', 'Folk'), ('LAT', 'Latin'), ('PUN', 'Punk'), ('RAP', 'Rap'), ('DSO', 'Disco'), ('FUN', 'Funk'), ('GOS', 'Gospel'), ('RB', 'R&B'), ('SOL', 'Soul'), ('TEC', 'Techno'), ('TRP', 'Trap')], default='ALT', max_length=3)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='main_app.song')),
                ('songs', models.ManyToManyField(related_name='genres', to='main_app.song')),
            ],
        ),
    ]