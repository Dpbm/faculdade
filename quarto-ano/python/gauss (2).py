def gauss(matrix):
    n = len(matrix)
    
    for i in range(n):
        max_row = i + max(range(n - i), key=lambda k: abs(matrix[i + k][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        
        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("Sistema não tem solução única.")
        
        for j in range(i + 1, n):
            ratio = matrix[j][i] / pivot
            for k in range(i, n + 1):
                matrix[j][k] -= ratio * matrix[i][k]
    
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]
    
    return x

matriz = [
    [3, 2, 4, 1],
    [1, 1, 2, 2],
    [4, 3, -2, 3]
]

solucao = gauss(matriz)
print("Solução do sistema:")
print(f"x1 = {solucao[0]}")
print(f"x2 = {solucao[1]}")
print(f"x3 = {solucao[2]}")