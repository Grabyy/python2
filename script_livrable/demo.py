"""Présente différentes possiblité offerte par le module pytest.

   On peut y voir démontrer des test unitaire basique sur des
   calcul ou un object. Un exemple d'utilisation des fixture,
   un exemple de récuperation d'exception par pytest.raises et
   et de parametrize fonction.
   Si l'on test ce script avec pytest on aura .....F ou les
   echecs (les  F) et par un test raté dans l'example de pytest.
   mark.parametrize.

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
        """Initialise l'atribut val à 0."""
        self._val = 0

    @property
    def get_val(self):
        """Renvoi l'attribut val."""
        return self._val

    def val_plus(self, ajout=1):
        """Ajoute la valeur de ajout a val.

        Par défaut, ajout vaut 1.
        """
        self._val += ajout


def test_assert_addition():
    """Demonstration de l'utilisation du mot clef assert.

    Test simplement si un plus un égale 2.
    """
    assert 1 + 1 == 2


def test_exception():
    """Demonstration de l'utilisation de pytest.raise().

    Verification de l'exception soulevé par la division
    par zéro via la methode raise de pytest.
    """
    with pytest.raises(ZeroDivisionError) as mon_ex:
        2 / 0
    assert "division par zero" in str(mon_ex.value)


@pytest.fixture(name="comp")
def fixture_comp():
    """Instanciation d'un compteur grace au decorator fixture."""
    return Compteur()


def test_compteur_init(comp):
    """Teste si le compteur s'initialise a 0."""
    assert comp.get_val == 0


def test_compteur_plus(comp):
    """Teste la methode val_plus de compteur."""
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

    Utilise comme argument les valeur initialiser avec le
    decorator pytest.mark.parametrize et effectue les test
    un a un avec ces valeurs.
    """
    assert (valeurs_test_1 + valeurs_test_2) == resultat_attendu


if __name__ == "__main__":
    pass
