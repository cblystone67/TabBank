from django.shortcuts import render
import requests

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def api_data(request):
    url = 'https://www.songsterr.com/a/ra/songs.json?pattern=master+of+puppets'
    
    response = requests.get(url)
    data = response.json()

    return render(request, 'about.html', {'data': data})
  