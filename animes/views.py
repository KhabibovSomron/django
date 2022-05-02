from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Anime, Genre


# Create your views here.
class AnimeView(ListView):
    """Список аниме"""
    model = Anime
    queryset = Anime.objects.filter(draft=False)
    template_name = "animes/animes.html"


class AnimeDetailView(DetailView):
    """Полное описание фильма"""
    model = Anime
    slug_field = "url"
