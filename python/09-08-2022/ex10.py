countSpaces = lambda a : sum([ 1 if letter.isspace() else 0 for letter in a ])

text = input("Texto: ")

print(countSpaces(text))