quadrados = lambda n: [ i ** 2 for i in range(1, n+1) ]

n = int(input())
print(*quadrados(n))