import re

remove_vogals = lambda text: re.sub('[aeiou]', '', text)

text = input("texto: ")

print(remove_vogals(text))