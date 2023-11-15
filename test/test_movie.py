import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from movie import Movie

def test_movie_instance():
    movie = Movie('Mean Girls', 'Cadie learns how to become a mean girl in high school', 5, True)
    clueless = Movie('Clueless', 'Shallow, rich and socially successful Cher is at the top of her Beverly Hills high school\'s pecking scale.', 5)
    assert isinstance(movie, Movie)
    assert isinstance(clueless, Movie)

def test_update_movie():
    star_wars = Movie('Star Wars', 'Luke Skywalker becomes a jedi', 5, True)
    star_wars.title = 'Star Wars - The Empire Strikes Back'
    assert star_wars.title == 'Star Wars - The Empire Strikes Back'

def test_default_seen():
    tiger = Movie('Crouching Tiger', 'In Qing dynasty China, Li Mu Bai and Yu Shu Lien lead a private security company', 4)
    et = Movie('E.T. the ExtraTerrestrial', 'E.T. lands on Earth and embarks on a new adventure with his human friends', 5, True)
    assert tiger.seen == False
    assert et.seen == True
