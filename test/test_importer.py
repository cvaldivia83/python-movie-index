import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from import_service import Importer

def test_importer():
    import_service = Importer('Indiana Jones')
    assert isinstance(import_service, Importer)

def test_importer_string():
    import_service = Importer('Indiana Jones')
    assert str(import_service) == 'IMPORTER - Movie import'

def test_importer_results():
    import_service = Importer('City Of God')
    assert len(import_service.fetch_movie()) == 2

def test_movie_import():
    import_service = Importer('Mean Girls')
    assert import_service.fetch_movie()[0] == 'Mean Girls'
    assert import_service.fetch_movie()[1] == 'Cady Heron is a hit with The Plastics, the A-list girl clique at her new school, until she makes the mistake of falling for Aaron Samuels, the ex-boyfriend of alpha Plastic Regina George.'
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from import_service import Importer

def test_importer():
    import_service = Importer('Indiana Jones')
    assert isinstance(import_service, Importer)

def test_importer_string():
    import_service = Importer('Indiana Jones')
    assert str(import_service) == 'IMPORTER - Movie import'

def test_importer_results():
    import_service = Importer('City Of God')
    assert len(import_service.fetch_movie()) == 2

def test_movie_import():
    import_service = Importer('Mean Girls')
    assert import_service.fetch_movie()[0] == 'Mean Girls'
    assert import_service.fetch_movie()[1] == 'Cady Heron is a hit with The Plastics, the A-list girl clique at her new school, until she makes the mistake of falling for Aaron Samuels, the ex-boyfriend of alpha Plastic Regina George.'
