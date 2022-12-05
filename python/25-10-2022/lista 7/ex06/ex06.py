import os
from itertools import product

get_combinations = lambda n: list(product('12', repeat=n))

def create_folders():
    inputExists = os.path.exists('./input')
    outputExists = os.path.exists('./output')

    if(not inputExists): os.makedirs('./input')
    if(not outputExists): os.makedirs('./output')

def get_result(combination):
    A = False
    B = False

    for i in combination:
        if i == '1': A = not A
        else: A, B = not A, not B

    return int(A), int(B)


if __name__ == '__main__':
    create_folders()

    counter = 1
    # nao rode com o range(1, 106) ou maior
    for n in range(1, 15):
        combinations = get_combinations(n)
        for combination in combinations:
            
            print(f"usando N = {n} e a combinação = {' '.join(combination)}")
            a, b = get_result(combination)
            print(f"resultado = {a}, {b}")

            input_data = f"{n}\n{' '.join(combination)}"
            output_data = f"{str(a)}\n{str(b)}"




            with open(f'./input/A_{counter}.txt', 'w') as input_arq:
                input_arq.write(input_data)
                print(f"escrito o arquivo de entrada A_{counter}")

            with open(f'./output/A_{counter}.txt', 'w') as output_arq:
                output_arq.write(output_data)
                print(f"escrito o arquivo de saida A_{counter}")

            counter += 1
            

