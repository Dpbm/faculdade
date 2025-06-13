# Matriz aumentada
A = [
   [3, 2, 4, 1],
   [1, 1, 2, 2],
   [4, 3, -2, 3]
]
n = len(A)
# Etapa de eliminação
for i in range(n):
   # Normalizar o pivô
   pivot = A[i][i]
   for k in range(i, n+1):
       A[i][k] = A[i][k] / pivot
   # Zerando abaixo do pivô
   for j in range(i+1, n):
       factor = A[j][i]
       for k in range(i, n+1):
           A[j][k] = A[j][k] - factor * A[i][k]
# Substituição retroativa
x = [0 for _ in range(n)]
for i in range(n-1, -1, -1):
   x[i] = A[i][n]
   for j in range(i+1, n):
       x[i] -= A[i][j] * x[j]
# Mostrar resultados
for idx, valor in enumerate(x, 1):
   print(f"x{idx} = {valor:.2f}")
print(A)