from random import sample

value = float(input('valor em R$: '))

numbers1 = int(input('valor 1: '))
numbers2 = int(input('valor 1: '))
numbers3 = int(input('valor 1: '))

equals = 0

values = [numbers1, numbers2, numbers3]

ale = sample(range(1, 5), 3)

print(f'values --> {values}\nale --> {ale}')

for index in values:
    if(macaco in ale):
        equals += 1

if(equals == 2):
    print(value * 5)
elif (equals == 3):
    print(value * 100)
else:
    print('se fudeu')
