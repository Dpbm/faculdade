from random import sample

valid_numbers = list(range(1, 50))

l1 = sample(valid_numbers, 10)
l2 = sample(valid_numbers, 10)

l3 = [0]*10

for i in range(10):
    if(i % 2 == 0):
        l3[i] = l1[i]
    else:
        l3[i] = l2[i]

print(*l1)
print(*l2)
print(*l3)