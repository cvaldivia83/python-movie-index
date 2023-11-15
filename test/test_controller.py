import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller import Controller
from database import Database

def test_controller():
    db = Database('../database.csv')
    cont = Controller(db)
    assert isinstance(cont, Controller)

def test_controller_string():
    db = Database('../database.csv')
    cont = Controller(db)
    assert str(cont) == 'CONTROLLER: Movie Controller'
