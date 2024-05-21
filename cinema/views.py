from datetime import datetime
from django.views.generic import TemplateView

from cinema import models


def normalize_number(number):
    if number // 10 == 0:
        number = '0' + str(number)
    return number


def get_current_date_time():
    current_date = datetime.now()
    current_day = current_date.day
    current_month = current_date.month
    current_year = current_date.year

    current_hour = current_date.hour
    current_minutes = current_date.minute

    current_day = normalize_number(current_day)
    current_month = normalize_number(current_month)
    current_hour = normalize_number(current_hour)
    current_minutes = normalize_number(current_minutes)
    dict_of_datetime = {
        "current_year": current_year,
        "current_day": current_day,
        "current_month": current_month,
        "current_hour": current_hour,
        "current_minutes": current_minutes
    }
    return dict_of_datetime


class FilmsView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = {
            'films': models.Movie.objects.all(),
            'genres': models.Genre.objects.all(),
            'title': 'Киноафиша',
            'datetime': get_current_date_time
        }
        return context


class GenreView(TemplateView):
    template_name = 'core/genre.html'

    def get_context_data(self, **kwargs):
        genre_id = kwargs['genre_id']
        films = models.Movie.objects.filter(genres=genre_id)
        genres = models.Genre.objects.all()
        count = models.Movie.objects.filter(genres=genre_id).count()
        datetime = get_current_date_time
        context = {
            'films': films,
            'genres': genres,
            'count': count,
            'datetime': datetime
        }
        return context


