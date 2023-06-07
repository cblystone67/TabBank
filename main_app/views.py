from django.shortcuts import render
import requests


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def search_index(request):
    url = 'https://www.songsterr.com/a/ra/songs.json?pattern=boat'
    
    response = requests.get(url)
    data = response.json()

    return render(request, 'search/index.html', {'data': data})

