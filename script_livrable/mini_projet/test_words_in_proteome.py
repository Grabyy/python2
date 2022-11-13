"""Programme de test pour le mini projet words_in_proteome.

   Ce script contient trois méthodes de test. On y retrouve
   des tests unitaires pour verifier les extentions des arguments
   et des tests d'intégrations pour verifier la création des objets.

Usage :
======
    python test_word_in_proteone.py
"""


import pytest
import words_in_proteome as word


@pytest.mark.parametrize(
    "filename, extention",
    [
        ("file1", ".txt"),
        ("file2", ".fasta"),
    ]
)
def test_extention_fichier(filename, extention, request):
    """Test l'extention des fichiers données en argument.

    Teste à la suite les extentions des deux fichiers donnée en
    argument (.txt pour la liste de mots et .fasta pour la séquence)
    """
    assert request.getfixturevalue(filename).endswith(extention)


def test_read_words(file1):
    """Test le retour de la fonction read_words.

    À partir du fichier donné en argument, vérifie la
    création d'une liste non vide.
    """
    result = word.read_words(file1)
    assert (result is not None) and (isinstance(result, list))


def test_read_sequences(file2):
    """Test le retour de la fonction read_sequences.

    À partir du fichier donné en argument, vérifie la
    création d'un dictionnaire non vide.
    """
    result = word.read_sequences(file2)
    assert (result is not None) and (isinstance(result, dict))


if __name__ == "__main__":
    pass
