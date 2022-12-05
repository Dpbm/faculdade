first_arq_name  = input("Nome do primeiro arquivo: ")
second_arq_name = input("Nome do segundo  arquivo: ")

with open("merge.txt", "w") as arq:

    first_arq  = open(first_arq_name,  'r')
    second_arq = open(second_arq_name, 'r')

    arq.write(first_arq.read() + "\n")
    arq.write(second_arq.read())

    first_arq.close()
    second_arq.close()
