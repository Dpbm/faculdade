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

print("\nTodos os dados inseridos\n")
for name, present in children.items():
    print(f'{name} {present}')

print("\nPorcentagem de crianças que pediram um celular\n")
print(f"total de crianças: {N}")
print(f"total de crianças que pediram celular: {total_phone}")
print(f"porcentagem final: {porcentage(N, total_phone):.2f}%") 