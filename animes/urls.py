from django.urls import path
from . import views

urlpatterns =[
    path("", views.AnimeView.as_view()),
    path("<slug:slug>/", views.AnimeDetailView.as_view(), name="anime_detail"),
    path("review/<int:pk>", views.AddReview.as_view(), name="add_review"),
]
