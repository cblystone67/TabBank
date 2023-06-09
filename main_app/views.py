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
'''
def scrape_songs():
    url = "https://www.guitaretab.com/fetch/?type=tab&query=Ed+Sheeran"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # Extract the songs and their details from the parsed HTML
        # For example, if the title and artist are within <h3> tags, you could do:
        songs = soup.find_all("h3")
        for song in songs:
            title = song.get_text()  # Extract the title
            artist = ""  # Extract the artist
            link = ""  # Extract the link
            # Create a new Song instance and save it to the database
            website = Website.objects.get(name="guitaretab.com")  # Get the Website instance
            Song.objects.create(title=title, artist=artist, link=link, website=website)
            
def songs_index(request):
    songs = Song.objects.filter(user=request.user)
    return render(request, 'songs/index.html', {'songs': songs})

def scrape_and_save_songs(request):
    if request.method == "POST":
        scrape_songs()  # Call the function to scrape and save the songs
    return redirect("index")  # Redirect to a suitable page after scraping and saving
  
'''
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


'''
def search_index(request):
    url = 'https://www.songsterr.com/a/ra/songs.json?pattern=boat'
    
    response = requests.get(url)
    data = response.json()

    return render(request, 'search/index.html', {'data': data})
'''
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

