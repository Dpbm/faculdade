from itertools import product
import sys

vowels = ('a', 'e', 'i', 'o', 'u')
consonants = ('d')

prepositions_singular = [ "".join(preposition) for preposition in list(product(consonants, vowels)) ]
prepositions_plural   = [ f'{preposition}s'    for preposition in prepositions_singular ]

articles_singular     = ('a', 'e', 'o') 
articles_plural       = [ f'{article}s' for article in articles_singular ]

all_prepositions_and_articles = [*articles_singular, *articles_plural, *prepositions_singular, *prepositions_plural]

name = [word.lower() 
            for word in input("nome completo: ").lower().split() 
            if word not in all_prepositions_and_articles
        ]

if(not len(name)):
    print("valor inválido!")
    sys.exit(1)

first = name[-1].upper()

rest  = ''

if(len(name) > 1):
    first += ','

    for actual_name in name[:-1]:
        rest += actual_name[0].upper() + '. '

print(f'{first} {rest}')