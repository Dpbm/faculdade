from random import randint

random_numbers = [ randint(1, 10) for _ in range(20) ]

x = int(input())

if(x < 1 or x > 10):
    print("valor invalido, aceitos valores de 1 a 10")
    exit()

print(*random_numbers)
print(f"{random_numbers.count(x)} iguais a {x} na lista")
