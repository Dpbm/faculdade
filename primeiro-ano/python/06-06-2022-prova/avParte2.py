"""
    Curso: BCC
    Data:  06/06/2022

    Problema:
    Escreva um programa que gereuma sequência de 10(correção 5 números) números inteiros, 
    entre 1 e 10, e os salve  em  uma lista.  Em  seguida  o  programa  
    deve  ler  um  número  inteiro  C.  O  programa deveentão encontrar 
    dois números de posições distintas da lista cuja multiplicação seja C e 
    imprimi-los. Caso não existam tais números, o programa deve imprimir uma 
    mensagem correspondente.

    Exemplo:
    Lista = [2, 4, 5, 10, 7]
    C = 35
    Resultado: 5 e 7
    
    Lista = [2, 4, 5, 10, 7]
    C = 25
    Resultado: não existem tais números
"""

from random import sample

C = int(input())
Lista = sample(list(range(1, 11)), 5)
valores = []

for i in range(len(Lista)):
    for j in range(len(Lista)):
        if Lista[i] * Lista[j] == C and Lista[i] != Lista[j]:
            valores = [Lista[i], Lista[j]]
            break
    
    if(len(valores)):
        break

print(f"\nLista = {Lista}")
print(f"C = {C}")

if(not len(valores)):
    print("Resultado: não existem tais números")
else:
    print(f"Resultado: {valores[0]} e {valores[1]}")
