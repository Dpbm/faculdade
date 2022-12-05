data = ""

while True:

    data += f"{input('nome da pessoa: ')} {input('telefone: ')}\n"

    if(input("continue [s/n]? ").lower() != 's'):
        break

with open("telephones.txt", "w") as arq:
    arq.write(data)

