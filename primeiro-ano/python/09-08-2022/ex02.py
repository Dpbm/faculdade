from unidecode import unidecode

sentence = input("Frase: ")

vogals = "aeiou"

toLower       = lambda a : a.lower()
removeAccents = lambda a : unidecode(a)
countVogals   = lambda a : sum([ a.count(letter) for letter in vogals ])

print(
    f'total --> {countVogals(toLower(removeAccents(sentence)))}'
)

