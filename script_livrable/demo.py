"""Présente différentes possibilités offerte par le module pytest.

   On peut y voir des tests unitaires basiques sur des scalaires ou un
   objet. Un exemple d'utilisation des fixtures, un exemple de test
   d'exception par pytest.raises et un exemple de parametrize fonction.
   Si l'on test ce script avec pytest on aura .....F où l'echec (le  F)
   et par un test raté dans l'example de pytest.mark.parametrize.

Usage :
======
    python demo.py

"""

__authors__ = ("Alexandre_Rizk", "Gabriel_Tourillon")
__contact__ = ("Mails")
__date__ = "21102022"
__version__ = "python_3.9"

import pytest


class Compteur:
    """Classe représentant un compteur utile pour nos exemples.

    Possède un attribut val qui s'incrémente grace a la méthode
    val_plus et une classe propietaire get_val pour récuperer val.
    """

    def __init__(self):
        """Constructeur de Compteur.

        Initialise l'attribut _val à 0.
        """
        self._val = 0

    @property
    def get_val(self):
        """Accesseur de l'attribut valeur.

        Renvoi l'attribut _val.
        """
        return self._val

    def val_plus(self, ajout=1):
        """Setteur de l'attribut val.

        Ajoute la valeur de ajout à val, par défaut, ajout vaut 1.
        """
        self._val += ajout


def test_assert_addition():
    """Demonstration de l'utilisation du mot clef assert.

    Test simplement si un plus un égale 2.
    """
    assert 1 + 1 == 2


def test_exception():
    """Demonstration de l'utilisation de pytest.raise().

    Vérification de l'exception soulevée par la division
    par zéro via la méthode raise de pytest.
    """
    with pytest.raises(ZeroDivisionError):
        print(2 / 0)


@pytest.fixture(name="comp")
def fixture_comp():
    """Instanciation d'un compteur grâce au décorateur fixture."""
    return Compteur()


def test_compteur_init(comp):
    """Teste si le compteur s'initialise à 0."""
    assert comp.get_val == 0


def test_compteur_plus(comp):
    """Teste la méthode val_plus de compteur."""
    comp.val_plus(5)
    assert comp.get_val == 5


@pytest.mark.parametrize(
    "valeurs_test_1, valeurs_test_2, resultat_attendu",
    [
        (1, 1, 2),
        (1, 1, 3)
    ]
)
def test_eval(valeurs_test_1, valeurs_test_2, resultat_attendu):
    """Test si les valeurs_test donne resultat_attendu.

    Utilise comme argument les valeurs initialisées avec le
    decorateur pytest.mark.parametrize et effectue les tests
    un à un avec ces valeurs.
    """
    assert (valeurs_test_1 + valeurs_test_2) == resultat_attendu


if __name__ == "__main__":
    pass
