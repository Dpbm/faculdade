"""
    Dupla:
    Alexandre Silva - 624071
    Gabriela Stela  - 628751 

    para rodar será necessário instalar o pandas
    rode: pip install pandas
"""

import pandas as pd

table = pd.DataFrame(columns=("k", "a", "b", "Xk", "f(a)", "f(Xk)", "sinal", "erro"))

f = lambda x : x**3 + 3*x - 1
get_Xk = lambda a,b : (a+b)/2
get_error = lambda a,b: b-a

precision = 0.001
a = 0
b = 1

steps = 0
max_steps = 10000000
error = b-a

while(error >= precision and steps < max_steps):

    Xk = get_Xk(a,b)
    f_a = f(a)
    f_Xk = f(Xk)
    signal = -1 if (f_a * f_Xk) < 0 else 1
    error = get_error(a,b)

    new_row = pd.Series({
        "k":steps, 
        "a":a, 
        "b": b,
        "Xk":Xk,
        "f(a)":f_a,
        "f(Xk)":f_Xk,
        "sinal":signal,
        "erro": error
        })

    table.loc[steps] = new_row

    if(f_a == 0):
        break
    elif(signal == 1):
        a = Xk
    elif(signal == -1):
        b = Xk

    steps += 1

root = table.loc[len(table)-1]["Xk"]


print(table)
print(f"raiz da função(Xk): {root}")