"""
    a --> 97
    z --> 122

    0 < shift < 26

    abcdefghijklmnopqrstuvwxyz

    teste, 6

    t --> 116 --> 116 + 6 --> 122
    u --> 117 --> 117 + 6 --> 123 --> 123 - 122
"""

shift_alphabet = lambda letter, shift : chr(ord(letter) + shift) if ord(letter) + shift <= 122 else chr(((ord(letter) + shift) - 123) + 97)
in_range = lambda letter:  ord(letter) >= 97 and ord(letter) <= 122 

def cesar(text, shift):
    if(shift < 0 or shift > 25):
        return

    return ''.join([ shift_alphabet(letter, shift) if (in_range(letter)) else letter for letter in text  ])


print(cesar('abcd xyz', 4))
    