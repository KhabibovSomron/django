from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Anime, Genre, Category
from .forms import ReviewForm

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
