toLower          = lambda a                 : a.lower()
countLetters     = lambda a, letter         : a.count(letter)
changeCharacters = lambda a, target, switch : a.replace(target, switch)

text = toLower(input("Texto: "))
letter1, letter2 = [ toLower(character) for character in input('Caracters: ').split()]

initialCount = countLetters(text, letter2)

print(f'Total --> { countLetters(changeCharacters(text, letter1, letter2), letter2) - initialCount }')