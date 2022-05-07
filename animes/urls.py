from django.urls import path
from . import views

urlpatterns =[
    path("", views.AnimeView.as_view()),
    path("filter/", views.FilterAnimeView.as_view(), name="filter"),
    path("search/", views.Search.as_view(), name="search"),
    path("add-rating/", views.AddStarRating.as_view(), name="add_rating"),
    path("<slug:slug>/", views.AnimeDetailView.as_view(), name="anime_detail"),
    path("review/<int:pk>", views.AddReview.as_view(), name="add_review"),
    path("character/<str:slug>", views.CharacterView.as_view(), name="character_datail"),
]
