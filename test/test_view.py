import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from view import View
from movie import Movie

def test_view():
    view = View()
    assert isinstance(view, View)

def test_view_string():
    view = View()
    assert str(view) == 'VIEW: User Interface'

def test_view_ask_user_name(monkeypatch):
    view = View()
    monkeypatch.setattr('builtins.input', lambda _: "Carla Valdivia")
    name = view.ask_user_name()
    assert name == 'Carla Valdivia'

def test_view_ask_user_for_stuff(monkeypatch):
    view = View()
    monkeypatch.setattr('builtins.input', lambda _: "Clueless")
    title = view.ask_user_for_stuff('title')
    assert title == 'Clueless'

def test_view_movie_seen_true(monkeypatch):
    view = View()
    monkeypatch.setattr('builtins.input', lambda _: "Y")
    movie_seen = view.ask_is_movie_seen()
    assert movie_seen == True

def test_view_movie_seen_false(monkeypatch):
    view = View()
    monkeypatch.setattr('builtins.input', lambda _: "N")
    movie_seen = view.ask_is_movie_seen()
    assert movie_seen == False

def test_view_rate_movie(monkeypatch):
    view = View()
    monkeypatch.setattr('builtins.input', lambda _: "1")
    rated = view.rate_movie()
    assert isinstance(rated, int)

def test_view_movie_rating(monkeypatch):
    view = View()
    monkeypatch.setattr('builtins.input', lambda _: "5")
    rating = view.movie_rating()
    assert isinstance(rating, int)

def test_view_ask_index(monkeypatch):
    view = View()
    monkeypatch.setattr('builtins.input', lambda _: "2")
    index = view.movie_rating()
    assert isinstance(index, int)

def test_view_display_imported_movie(monkeypatch):
    view = View()
    list = ['The Hitchhiker\'s Guide to the Galaxy', 'The answer to life, universe and everything is 42']
    monkeypatch.setattr('builtins.input', lambda _: "Y")
    display = view.display_imported_movie(list)
    assert display == True

def test_view_list_all_movies(capsys):
    list = []
    view = View()
    movie = Movie('Interstellar', 'When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.', 5, True)
    list.append(movie)
    view.list_all_movies(list)
    captured = capsys.readouterr()
    output_lines = captured.out.split('\n')
    assert output_lines[0] == '1 - [X] - Interstellar - 5/5 '
    assert output_lines[1] == ' => When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans. '
