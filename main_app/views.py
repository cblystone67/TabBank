from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Song
#from bs4 import BeautifulSoup
import requests


# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def songs_index(request):
  songs = Song.objects.filter(user=request.user)
  return render(request, 'songs/index.html', {'songs': songs})

def songs_details(request, song_id):
  song = Song.objects.get(id=song_id)
  return render(request, 'songs/details.html', {'song': song})


def fetch_data(request):
    api_url = 'https://www.songsterr.com/a/ra/songs.json?pattern=shiver'
    
    response = requests.get(api_url)
    data = response.json()

    return render(request, 'songs/results.html', {'data': data})

class SongCreate(CreateView):
  model = Song
  fields = ['title', 'artist']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class SongUpdate(UpdateView):
  model = Song
  fields = ['title', 'artist']
  
class SongDelete(DeleteView):
  model = Song
  success_url = '/songs/'
  
  
def signup(request):
  error_message = ''
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('about')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {'form': form, 'error': error_message} )

