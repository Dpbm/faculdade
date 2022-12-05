changeLetter = lambda a : chr(ord(a) + 1)

text = input("Texto: ")

print(''.join([ changeLetter(letter) for letter in text ]))