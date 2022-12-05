from random import randint

card = []
all_values = []
j = 0

for i in range(5):

    card.append([])

    j = 0
    while len(card[-1]) != 5:
        if(i == 2 and j == 2 and card[i][-1] != "C"):
            card[i].append("C")
            continue


        start_value = j * 15 + 1
        end_value = (j + 1) * 15


        value = randint(start_value, end_value)
        
        if(value in all_values):
            continue

        card[i].append(value)
        all_values.append(value)


        j += 1   

for i in card:
    for j in i:
        print((f'{j:02}' if type(j) == int else "CC"), end=" ")
    print()