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
    argument (.txt pour les mots et .fasta pour la séquence)
    """
    assert request.getfixturevalue(filename).endswith(extention)


def test_read_words(file1):
    """Test le retour des fonctions"""
    result = word.read_words(file1)
    assert (result is not None) and (type(result) == list)


def test_read_sequences(file2):
    """Test le retour des fonctions"""
    result = word.read_sequences(file2)
    assert (result is not None) and (type(result) == dict)
