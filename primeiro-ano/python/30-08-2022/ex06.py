from random import sample

generate_matrix = lambda m,n : [ sample(list(range(10)), n) for _ in range(m)  ]
max_column_value = lambda matrix, col_n : max([ matrix[i][col_n] for i in range(len(matrix)) ])
min_row_value = lambda matrix, row_n : min(matrix[row_n])

matrix = generate_matrix(10, 10)

for row in matrix:
    print(row)

print(max_column_value(matrix, 1))
print(min_row_value(matrix, 0))