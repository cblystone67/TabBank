from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
  title = models.CharField(max_length=50)
  artist = models.CharField(max_length=50)
  
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  #link = models.URLField()
  #website = models.ForeignKey(Website, on_delete=models.CASCADE)
  def __str__(self):
    return (self.title)
  
  def get_absolute_url(self):
      return reverse("details", kwargs={"song_id": self.id})
  
class Genre(models.Model):
  STYLES = (
    ('ALT', 'Alternative'),
    ('BLU', 'Blues'),
    ('CLC', 'Classical'),
    ('CNY', 'Country'),
    ('EDM', 'Electronic Dance Music'),
    ('HIP', 'Hip Hop'),
    ('JAZ', 'Jazz'),
    ('MTL', 'Metal'),
    ('POP', 'Pop'),
    ('RNB', 'Rhythm and Blues'),
    ('RCK', 'Rock'),
    ('REG', 'Reggae'),
    ('IND', 'Indie'),
    ('FOL', 'Folk'),
    ('LAT', 'Latin'),
    ('PUN', 'Punk'),
    ('RAP', 'Rap'),
    ('DSO', 'Disco'),
    ('FUN', 'Funk'),
    ('GOS', 'Gospel'),
    ('RB', 'R&B'),
    ('SOL', 'Soul'),
    ('TEC', 'Techno'),
    ('TRP', 'Trap'),
  )
  name = models.CharField(max_length=255)
  songs = models.ManyToManyField(Song, related_name='genres')
  style = models.CharField(
    max_length=3,
    choices=STYLES,
    default=STYLES[0][0])
  
  song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='genre')
  
  def __str__(self) -> str:
     return f"{self.get_style_display()} on {self.style}"
  