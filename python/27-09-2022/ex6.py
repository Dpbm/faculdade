leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

N = int(input())

results = []

calc_leds_amount = lambda x : sum([ leds[int(i)] for i in x ])

for test in range(N):
    V = int(input())
    results.append(calc_leds_amount(str(V)))

for i in results:
    print(f"{i} leds")