from django.urls import path
from .views import RegisterUserView, MovieListCreateView, MovieDeleteView, MovieToggleWatchedView


# Urls for user registration, movie list, create and delete, and toggle watched status
urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDeleteView.as_view(), name='movie-delete'),
    path('movies/<int:pk>/toggle-watched/', MovieToggleWatchedView.as_view(), name='movie-toggle-watched'),
]