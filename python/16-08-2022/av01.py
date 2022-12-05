from collections import defaultdict
from unidecode import unidecode

def remove_punctuation(word):
    punctuations = (".",  ",",  ":",  ";",  "!",  "?")
    
    for punctuation in punctuations:
        word = word.replace(punctuation, '')
    
    return word 

palindromes = defaultdict(int)

text = [unidecode(remove_punctuation(word)) for word in input().lower().split()]

for word in text:
    if word == word[::-1] and len(word) >= 3:
        palindromes[word] += 1

for palindrome in dict(palindromes).keys():
    quantity = palindromes[palindrome]
    print(f'{palindrome} {quantity}')


