from random import sample, randint

A = sample(list(range(0, 50)), randint(1, 6))
B = sample(list(range(0, 50)), randint(1, 6))
equals = []

biggest = []
smallest = []

if(len(A) > len(B)):
    biggest = A
    smallest = B
else:
    biggest = B
    smallest = A

for i in biggest:
    if(i in smallest):
        equals.append(i)

print(*A)
print(*B)
print(*equals)