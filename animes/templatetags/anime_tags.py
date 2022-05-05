import re
from django import template
from animes.models import Category, Anime


register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категирий"""
    return Category.objects.all()


@register.inclusion_tag('animes/tags/last_anime.html')
def get_last_animes(count=5):
    animes = Anime.objects.order_by("id")[:count]
    return {"last_animes": animes}