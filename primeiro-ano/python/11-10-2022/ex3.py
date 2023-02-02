filter_numbers     = lambda w: filter(even_index_numbers, enumerate(w))
even_index_numbers = lambda element: element[0] % 2 == 0
get_numbers        = lambda packed_array: [number for _, number in packed_array ]

get_even_index_numbers_only = lambda w: get_numbers(filter_numbers(w))

indices_pares      = lambda w: get_even_index_numbers_only(w)

print(indices_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))