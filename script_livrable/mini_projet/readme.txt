=====       Utilisation de pytest sur ce projet       =====


Afin de tester les fichiers ainsi que le fonctionnement du mini projet, des options
on été définie dans le fichier de configuration conftest.py. Le conftest.py est donc
obligatoire pour le bon fonctionnement du script de test.


Les options définies sont :

option --file1 pour les mot (.txt)
option --file2 pour les séquence (.fasta)



TLDR :

pytest test_words_in_proteome.py --file1 english-common-words.txt --file2 human-proteome.fasta

ou

python -m pytest test_words_in_proteome.py --file1 english-common-words.txt --file2 human-proteome.fasta

