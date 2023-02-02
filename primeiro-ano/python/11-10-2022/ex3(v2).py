
indices_pares      = lambda w: [value for index, value in enumerate(w) if index % 2 == 0 ]

print(indices_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))