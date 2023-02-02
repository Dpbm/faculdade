changeLetter = lambda a : chr(ord(a) + 3)

text = input("Texto: ")

print(''.join([ changeLetter(letter) if letter.isalpha() else letter for letter in text ]))