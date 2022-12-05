import sys
from math import sqrt

a, b, c = [float(i) for i in input("a - b - c\n").split()]

if(not a):
    print("Não há raiz para essa equação!")
    sys.exit(0)

delta = lambda a, b, c : b**2 - 4 * a * c

x1    = lambda delta, a, b: (-b + sqrt(delta)) / (2 * a)
x2    = lambda delta, a, b: (-b - sqrt(delta)) / (2 * a)

try:

    delta_number = delta(a, b, c)
    x1_value = x1(delta_number, a, b)
    x2_value = x2(delta_number, a, b)


    print(x1_value, x2_value)
except:
    print("erro ao tentar cálcular os valores!")
    sys.exit(1)