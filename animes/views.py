from re import template
from statistics import mode
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Anime, Character, Genre, Category
from .forms import ReviewForm

# Create your views here.

class GenreYear:
    """Жанры и года выхода аниме"""
    def get_genres(self):
        return Genre.objects.all()
    
    def get_years(self):
        return Anime.objects.filter(draft=False).values("year")

class AnimeView(GenreYear, ListView):
    """Список аниме"""
    model = Anime
    queryset = Anime.objects.filter(draft=False)
    template_name = "animes/animes.html"


class AnimeDetailView(GenreYear, DetailView):
    """Полное описание фильма"""
    model = Anime
    slug_field = "url"


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        print(request.POST)
        form = ReviewForm(request.POST)
        anime = Anime.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.anime = anime
            form.save()
        return redirect(f"/{anime.url}/")


class CharacterView(GenreYear, DetailView):
    """ Вывод информации о персонаже """
    model = Character
    template_name = "animes/character.html"
    slug_field = "name"


class FilterAnimeView(GenreYear, ListView):
    """Фильтр аниме"""
    template_name = "animes/animes.html"
    def get_queryset(self):
        print(self.request.GET.getlist("genre"))
        if self.request.GET.getlist("genre") and self.request.GET.getlist("year"):
            queryset = Anime.objects.filter(
                year__in=self.request.GET.getlist("year"),
                genres__in=self.request.GET.getlist("genre")
                )
        elif self.request.GET.getlist("year"):
            queryset = Anime.objects.filter(year__in=self.request.GET.getlist("year"))
        elif self.request.GET.getlist("genre"):
            queryset = Anime.objects.filter(year__in=self.request.GET.getlist("genre"))
        else:
            queryset = Anime.objects.all()
        return queryset