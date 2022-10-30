---       Utilisation de pytest sur ce projet       ---





-----------               Le config.py est obigatoire, c'est la que les fixture et les option sont definie

option --file1 pour les mot (.txt)
option --file2 pour les séquence (.fasta)




TLDR : 

pytest test_words_in_proteome.py --file1 english-common-words.txt --file2 human-proteome.fasta

ou

python -m pytest test_words_in_proteome.py --file1 english-common-words.txt --file2 human-proteome.fasta

