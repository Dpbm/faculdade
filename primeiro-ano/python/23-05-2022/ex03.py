# (n + n** 3) / 2
magic_cube = []

def magic_cube_calc(n):
    return (n + n **3) / 2

N = int(input("N: "))


for i in range(N):
    magic_cube.append([  int(i)  for i in input().split()  ])

is_a_magic_cube = True
calc_total_to_be_a_magic_cube = magic_cube_calc(N)

diagonal = [magic_cube[i][N - 1 - i] for i in range(N)]
if sum(diagonal) != calc_total_to_be_a_magic_cube:
    is_a_magic_cube = False

if(is_a_magic_cube):
    for i in range(N):

        column = [magic_cube[j][i]  for j in range(N) ]

        
        if sum(magic_cube[i]) != calc_total_to_be_a_magic_cube or sum(column) != calc_total_to_be_a_magic_cube:
            is_a_magic_cube = False
            break

print('magic cube' if is_a_magic_cube else "it's not a magic cube")



    