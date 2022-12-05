a = [3, 5, 7, 9, 11]
b = [1, 3, 6, 9, 12]
c = []

k = 1
for i in range(5):
    x = 0
    for j in range(5):
        if a[i] == b[j]:
            x = 1
    if x == 0:
        c.append(a[i])

print(c)