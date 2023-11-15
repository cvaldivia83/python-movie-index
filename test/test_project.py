import pytest
import sys
import os
from project import actions
from project import router
from database import Database
from controller import Controller

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_actions(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    call = actions()
    assert call == 1

def test_router_add_movie(monkeypatch):
    csv_path = '../database.csv'
    database = Database(csv_path)
    controller = Controller(database)
    inputs = ['It', 'Killer Clown takes over a small city', '3', 'N']
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda prompt: next(input_generator))
    router(2, controller)
    assert database.movies[-1].title == 'It'

def test_router_delete_movie(monkeypatch):
    csv_path = '../database.csv'
    database = Database(csv_path)
    before_db_movies = len(database.movies)
    controller = Controller(database)
    monkeypatch.setattr('builtins.input', lambda _: "1")
    router(3, controller)
    assert before_db_movies - 1 == len(database.movies)

def test_router_mark_seen(monkeypatch):
    csv_path = '../database.csv'
    database = Database(csv_path)
    controller = Controller(database)
    monkeypatch.setattr('builtins.input', lambda _: "1")
    rout = router(4, controller)
    assert database.movies[0].seen == True


def test_router_rate_movie(monkeypatch):
    csv_path = '../database.csv'
    database = Database(csv_path)
    controller = Controller(database)
    inputs = [1, 1]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda prompt: next(input_generator))
    router(5, controller)
    assert database.movies[0].rating == 1

def test_router_export_list(monkeypatch):
    csv_path = '../database.csv'
    database = Database(csv_path)
    controller = Controller(database)
    monkeypatch.setattr('builtins.input', lambda _: "andre")
    router(7, controller)
    assert os.path.isfile('andre_movie_index.pdf')
