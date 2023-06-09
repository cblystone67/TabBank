from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now



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
  style = models.CharField(
    max_length=3,
    choices=STYLES,
    default=STYLES[0][0])
  
  def __str__(self) -> str:
     return f"{self.get_style_display()} on {self.style}"


class Song(models.Model):
  title = models.CharField(max_length=50)
  artist = models.CharField(max_length=50)
  
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  genres = models.ManyToManyField(Genre, related_name='songs')
  
  def __str__(self):
    return (self.title)
  
  def get_absolute_url(self):
      return reverse("details", kwargs={"song_id": self.id})

  
class Comments(models.Model):
  song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='comments', default=1)
  comment_text = models.TextField(default=now)
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  
  created_at = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self) -> str:
    return self.comment_text[:50] + '...' if len(self.comment_text) > 50 else self.comment_text
  class Meta:
    ordering = ['-song__created_at']
  
  