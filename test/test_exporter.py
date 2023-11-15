import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from export_service import Exporter
from movie import Movie

def test_exporter():
    username = 'Andre'
    movie1 = Movie("Mean Girls", "Cady Heron arrives in the US and has to learn how to survive in an american high school. In the meanwhile she fights not to become a mean girl.", 2, True)

    movie2 = Movie("Indiana Jones", "Famous archeologist Indiana Jones goes to Egypt and tries to find the treasure in the secret cave.", 3, False)

    movie3 = Movie("Nikita", "Woman spy Nikita received training to become the best spy in the world. History will tell if she will succeed in the real world.", 4, True)

    movies = [movie1, movie2, movie3]
    exporter = Exporter(movies, username)
    assert isinstance(exporter, Exporter)

def test_exporter_string():
    username = 'Chloe'
    movie1 = Movie("Mean Girls", "Cady Heron arrives in the US and has to learn how to survive in an american high school. In the meanwhile she fights not to become a mean girl.", 2, True)

    movie2 = Movie("Indiana Jones", "Famous archeologist Indiana Jones goes to Egypt and tries to find the treasure in the secret cave.", 3, False)

    movies = [movie1, movie2]
    exporter = Exporter(movies, username)
    assert str(exporter) == 'EXPORTER - Chloe Movie PDF exporter'

def test_export_file():
    username = 'Cristina'
    movie1 = Movie("Mean Girls", "Cady Heron arrives in the US and has to learn how to survive in an american high school. In the meanwhile she fights not to become a mean girl.", 2, True)

    movie2 = Movie("Indiana Jones", "Famous archeologist Indiana Jones goes to Egypt and tries to find the treasure in the secret cave.", 3, False)

    movies = [movie1, movie2]
    exporter = Exporter(movies, username)
    exporter.export_pdf()
    assert os.path.isfile('cristina_movie_index.pdf')
