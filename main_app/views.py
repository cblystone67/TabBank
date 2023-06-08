from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Song
from django.shortcuts import render, redirect
import requests


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def search_index(request):
  songs = Song.objects.all()
  return render(request, 'search/index.html', {'songs': songs})

'''
def search_index(request):
    url = 'https://www.songsterr.com/a/ra/songs.json?pattern=boat'
    
    response = requests.get(url)
    data = response.json()

    return render(request, 'search/index.html', {'data': data})
'''
def signup(request):
  error_message = ''
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {'form': form, 'error': error_message} )

