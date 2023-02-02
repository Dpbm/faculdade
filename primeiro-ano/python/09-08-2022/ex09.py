changeZeroToOne = lambda a : a.replace('0', '1')

text = input("Texto: ")

print( text, changeZeroToOne(text) )