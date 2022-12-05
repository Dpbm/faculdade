is_an_even_index = lambda i: i % 2 == 0
filter_w_list    = lambda w: list(filter(lambda l : is_an_even_index(l[0]), list(enumerate(w))))

indices_pares = lambda w: [ i[1] for i in filter_w_list(w) ] 

w = [1, 4, 12, 32, 5, 6, 12]

print(indices_pares(w))