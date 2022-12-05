from random import randint

l = [ randint(1, 50) for _ in range(20) ]

x = int(input())

if(x in l):
    print(f"existe o valor {x} na lista {l}")
    l = list(filter((lambda y : y != x), l))
    print(f"nova lista sem o valor {x} = {l}")
    exit()

print(f"não existe o valor {x} na lista {l}")
