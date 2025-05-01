"""
    Alunos:
    Alexandre Silva - 624071
    Gabriela Stela  - 628751
"""

from math import exp

fun = lambda x : exp(-1 * (x**2)) - x
fun_dx = lambda x: -2 * x * exp(-1 * (x**2)) - 1

next_x = lambda xn : xn - (fun(xn) / fun_dx(xn))

xn = 0
i = 1
MAX_ITER = 10000

while i < MAX_ITER:
    next_value = round(next_x(xn), 8)
    
    print(f"i:{i}; xn: {xn}; xn+1:{next_value}")
    
    if(next_value == xn):
        break

    xn = next_value
    i += 1

if(i == MAX_ITER):
    print("Solução noi foi encontrada")
    print(f"Valor final: {xn}")
else:
    print(f"raiz={xn}") 
