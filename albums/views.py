from urllib import request
from django.shortcuts import render

from .models import Albums

def list(request):
    all_albums = Albums.objects.all()
    return render(request, 'albums/albums_list.html', {'albums': all_albums})
