from operator import mul
from functools import reduce

prod_lista = lambda lista : reduce(mul, lista)

print(prod_lista([1, 2, 3, 4]))