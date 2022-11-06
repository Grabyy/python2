"""Script de configuration pour tester word_in_proteome.py.

    Deux arguments de pytest dont définie, --file1 et --file2.
    Ils permettent de crée des fixture qui nous aideront à tester
    si le code du mini project fonctionne avec des fichier.
    spécifiques

Usage :
======
    python demo.py

"""

__authors__ = ("Alexandre_Rizk", "Gabriel_Tourillon")
__contact__ = ("Mails")
__date__ = "21102022"
__version__ = "python_3.9"


import pytest


def pytest_addoption(parser):
    """Définie deux nouveaux arguments pour pytest."""
    parser.addoption("--file1", action="store")
    parser.addoption("--file2", action="store")


@pytest.fixture(scope='session')
def file1(request):
    """Création d'une fixture pour --file1."""
    filename = request.config.option.file1
    if filename is None:
        pytest.skip()
    return filename


@pytest.fixture(scope='session')
def file2(request):
    """Création d'une fixture pour --file2."""
    filename = request.config.option.file2
    if filename is None:
        pytest.skip()
    return filename
