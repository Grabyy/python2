"""Script de configuration pour tester word_in_proteome.py.

    Deux arguments de pytest sont définie, --file1 et --file2.
    Ils permettent de créer des fixtures qui nous aideront à tester
    le code du mini projet fonctionne avec des fichiers spécifiques.

Usage :
======
    python conftest.py

"""

__authors__ = ("Alexandre_Rizk", "Gabriel_Tourillon")
__contact__ = ("Mails")
__date__ = "21102022"
__version__ = "python_3.9"


import pytest


def pytest_addoption(parser):
    """Définie deux nouvelles options pour pytest.

    option : --file1 & --file2
    """
    parser.addoption("--file1", action="store")
    parser.addoption("--file2", action="store")


@pytest.fixture(scope='session')
def file1(request):
    """Création d'une fixture pour --file1.

    Récupère le fichier donné dans l'arguments --file1,
    et crée une fixture qui permet d'y accéder.
    """
    filename = request.config.option.file1
    if filename is None:
        pytest.skip()
    return filename


@pytest.fixture(scope='session')
def file2(request):
    """Création d'une fixture pour --file2.

    Récupère le fichier donné dans l'arguments --file2,
    et crée une fixture qui permet d'y accéder.
    """
    filename = request.config.option.file2
    if filename is None:
        pytest.skip()
    return filename
