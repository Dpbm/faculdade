text = input("Texto: ")
letter = input('Caractere:')

toLower       = lambda a    : a.lower()

countLetter   = lambda a, b : a.count(b)

print(f'total --> {countLetter( toLower(text), letter )}')