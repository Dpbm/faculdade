from copy import deepcopy

A = [
    [10, 1, 1],
    [1, 10, 1],
    [1, 1, 10]
]

b = [
    12,
    12,
    12
]


current = [
    0,
    0,
    0
]

last_current = deepcopy(current)

x = lambda c: 1/A[0][0] * (b[0] - c[1] - c[2])
y = lambda c: 1/A[1][1] * (b[1] - c[0] - c[2])
z = lambda c: 1/A[2][2] * (b[2] - c[0] - c[1])

max_error = 10e-3

def reached_min_error():
    return all([ abs(current[i] - last_current[i]) < max_error for i in range(3) ])


def one_step():
    current[0] = x(current)
    current[1] = y(current)
    current[2] = z(current)

iterations = 0

while True:
    one_step()

    if reached_min_error():
        break

    last_current = deepcopy(current)

print(
    f"""
    Valores aproximados para as incógnitas:
    x ~ {round(current[0])}
    y ~ {round(current[1])}
    z ~ {round(current[2])}
    """
)