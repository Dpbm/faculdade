N = int(input())

def calculate_difference (p1, p2): 
    max_high = max([ p1[i] + p2[i] for i in range(len(p1)) ])

    return sum([ max_high - (p1[i] + p2[i])  for i in range(len(p1)) ])


def calculate(p1, p2):

    if(len(p1) == len(p2)): return calculate_difference(p1, p2), 1

    increment = 0
    smallest_difference = calculate_difference(p1, p2[:len(p1)])
    smallest_difference_position = 1

    while increment + len(p1) <= len(p2):
        
        difference = calculate_difference(p1, p2[increment:len(p1)+increment])

        if(difference < smallest_difference):
            smallest_difference = difference
            smallest_difference_position = increment + 1
    
        increment += 1

    return smallest_difference, smallest_difference_position 


    

parts = [ 
    (list(map(int, input().split())), list(map(int, input().split())))  
    for _ in range(N) 
]

for p1, p2 in parts:
    pontuation_normal, position_normal     = calculate(p1, p2)
    pontuation_inverted, position_inverted = calculate(p1[::-1], p2)


    
    pontuation = pontuation_normal if pontuation_normal < pontuation_inverted else pontuation_inverted
    position = position_normal if pontuation_normal < pontuation_inverted else position_inverted
    direction = "Normal" if pontuation_normal <= pontuation_inverted else "Invertida"

    if(not pontuation): print("Encaixe Perfeito!")
    else: print(f"Pontuacao: {pontuation}")
    print(f"Posicao de Encaixe: {position}")
    print(f"Peca 1: {direction}")
   
    
