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

max_error = 10**(-3)

def reached_min_error():
    return all([ abs(current[i] - last_current[i]) < max_error for i in range(3) ])

def one_step():
    current[0] = x(current)
    current[1] = y(current)
    current[2] = z(current)

def show_current(i):
    print(f"x({i}) = {current[0]}")
    print(f"y({i}) = {current[1]}")
    print(f"z({i}) = {current[2]}")
    print()

def sassenfeld():
    previous = []
    for i in range(3):
        row = A[i]
        diagonal_value = row[i]
        other_values = [ row[j] for j in range(3) if j != i ]

        if(i >= 1):
            other_values[0] *= previous[0]
        if(i == 2):
            other_values[1] *= previous[1]

        other_values_sum = sum(other_values)
        convergence = other_values_sum / diagonal_value

        previous.append(convergence)

        print(f"convergencia linha {i+1}: {convergence}")

        if convergence >= 1:
            return False

    return True

if not sassenfeld():
    print("Não Garante convergência")
    exit()

print("Garante convergência\n")


iterations = 0
while True:
    show_current(iterations)
    one_step()

    if reached_min_error():
        show_current(iterations+1)
        break

    last_current = deepcopy(current)
    iterations += 1

print(
    f"""
    Valores aproximados para as incógnitas:
    x ~ {round(current[0])}
    y ~ {round(current[1])}
    z ~ {round(current[2])}
    """
)