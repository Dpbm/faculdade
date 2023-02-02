porcentage = lambda total, part: (part / total) * 100 

children = {}
total_phone = 0

N = int(input("Quantidade de Crianças: "))

for _ in range(N):
    name = input("Nome da criança: ")
    present = input("Presente: ")

    children[name] = present

    if(present == 'celular'):
        total_phone += 1

print("\n*********Todos os dados inseridos*********")
for name, present in children.items():
    print(f'{name} pediu {present}')

print("\n*********Porcentagem de crianças que pediram um celular*********")
print(f"total de crianças: {N}")
print(f"total de crianças que pediram celular: {total_phone}")
print(f"porcentagem final: {porcentage(N, total_phone):.2f}%") 