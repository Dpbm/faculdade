from functools import reduce

words = {}

translate_to_portuguese = lambda word, words: words.get(word, "Palavra não encontrada")
translate_to_english    = lambda word, words: list(filter(lambda packed_words: packed_words[1] == word,   list(words.items())))[0][0]

N = int(input())

for _ in range(N):
    portuguese_word = input("Palavra em português: ").lower()
    english_word    = input("Tradução em inglês:   ").lower()

    words[english_word] = portuguese_word

while True:
    translate_to = input("Tradução para [p/i]: ")
    word         = input("Palavra: ").lower()
    
    if(translate_to == 'p'): print(translate_to_portuguese(word, words))
    else: print(translate_to_english(word, words))


    if(input("Continuar ") != 's'):
        break