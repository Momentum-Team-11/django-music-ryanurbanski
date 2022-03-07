import re
from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Albums

class AlbumsListView(ListView):
    model = Albums
    context_object_name = 'albums'
    template_name = 'albums/albums_list.html'

class AlbumsDetailView(DetailView):
    model = Albums
    context_object_name = 'album'
    # template_name = 'albums/albums_detail.html'
