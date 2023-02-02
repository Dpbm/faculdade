value = int(input('valor: '))

banknotes_total = {
    '50': 0,
    '10': 0,
    '5': 0,
    '1':0
}

values = [50, 10, 5, 1]
actual = 0

while value > 0:
    if(value // values[actual] > 0):
        banknotes_total[str(values[actual])] += value // values[actual]
        value %= values[actual]
    else:
        actual += 1
    

print(banknotes_total)