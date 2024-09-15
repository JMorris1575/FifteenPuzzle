from django.urls import path

from .views import entry_view, puzzle_view, clock_view, game_view

app_name = 'fifteen'
urlpatterns = [
    path('entry/', entry_view, name='entry'),
    path('puzzle/', puzzle_view, name='puzzle'),
    path('clock/', clock_view, name='clock'),
    path('game/', game_view, name='game'),
]
