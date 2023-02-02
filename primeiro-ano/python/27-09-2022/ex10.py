from functools import reduce

l = [1, 2, 3, 4]

prod_lista = reduce(lambda a, b : a * b, l)
print(prod_lista)