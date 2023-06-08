from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date



# Create your models here.

class Song(models.Model):
  title = models.CharField(max_length=50)
  artist = models.CharField(max_length=50)
  
  
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return (self.title)
  
  