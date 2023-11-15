import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import Database
from movie import Movie

csv_path = '../database.csv'

def test_database():
    db = Database(csv_path)
    assert isinstance(db, Database)

def test_wrong_csv():
    with pytest.raises(FileNotFoundError):
        db = Database('database.csv')

def test_db_string():
    db = Database(csv_path)
    assert str(db) == 'DATABASE: MovieIndex DB'

def test_db_array():
    with open(csv_path, 'w') as file:
        pass
    db = Database(csv_path)
    assert db.movies == []

def test_db_create():
    with open(csv_path, 'w') as file:
        pass
    db = Database(csv_path)
    godfather = Movie('The Godfather', 'A drama about the Corleone Family and the Italian Mafia', 5, True)
    db.create(godfather)
    assert len(db.movies) == 1

def test_db_destroy():
    with open(csv_path, 'w') as file:
        pass
    db = Database(csv_path)
    godfather = Movie('The Godfather', 'A drama about the Corleone Family and the Italian Mafia', 5, True)
    elvira = Movie('Elvira, Mistress of The Dark', 'TV horror hostess Elvira goes back to a small city to claim her fortune', 5, True)
    db.create(godfather)
    db.create(elvira)
    db.destroy(0)
    assert len(db.movies) == 1
    assert db.movies[0].title == 'Elvira, Mistress of The Dark'
