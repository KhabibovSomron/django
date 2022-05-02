from django.urls import path
from . import views

urlpatterns =[
    path("", views.AnimeView.as_view()),
    path("<slug:slug>/", views.AnimeDetailView.as_view(), name="anime_detail"),
]
