def power(value, p):
    if(p == 1):
        return value
    return value * power(value, p - 1)

print(power(3, 3))