from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('songs/', views.songs_index, name='index'),
  path('fetch/', views.fetch_data, name='fetch-data'),
  path('songs/<int:song_id>/', views.songs_details, name='details'),
  path('songs/create', views.SongCreate.as_view(), name='songs_create'),
  path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
  path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
  path('account/signup/', views.signup, name='signup'),
]
