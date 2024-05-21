from django.urls import path
import cinema.views

urlpatterns = [
    path('', cinema.views.FilmsView.as_view()),
    path('genres/<int:genre_id>/', cinema.views.GenreView.as_view()),
]
