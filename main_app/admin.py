from django.contrib import admin
from .models import Song, Genre, Comments
# Register your models here.

admin.site.register([Song, Genre, Comments])