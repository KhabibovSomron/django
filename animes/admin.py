from django.contrib import admin

# Register your models here.
from .models import Category, Character, Genre, Anime, AnimeShots, Rating, RatingStar, Reviews

admin.site.register(Category)
admin.site.register(Character)
admin.site.register(Genre)
admin.site.register(Anime)
admin.site.register(AnimeShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
