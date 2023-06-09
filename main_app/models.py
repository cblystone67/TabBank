from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import requests
#from bs4 import BeautifulSoup





# Create your models here.
'''
class Website(models.Model):
  name = models.CharField(max_length=255)
'''

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
  