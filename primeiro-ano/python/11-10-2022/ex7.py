from random import randint

generate_matrix = lambda n, m:         [[randint(0, 10) for _ in range(m)] for __ in range(n)]
flat_matrix     = lambda matrix, n, m: [matrix[i][j] for j in range(m) for i in range(n)]

m = n = 10
matrix = generate_matrix(m, n)
print(flat_matrix(matrix, n, m))