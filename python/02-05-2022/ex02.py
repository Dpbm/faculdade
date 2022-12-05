from random import sample, randint

A = sample(list(range(0, 50)), randint(1, 6))
B = sample(list(range(0, 50)), randint(1, 6))
equals = []

for i in [*A, *B]:
    if i not in equals:
        equals.append(i)

print(*A)
print(*B)
print(*equals)