
while True:
    primeiro = int(input('cu: '))
    segundo = int(input('cu2: '))

    if(primeiro < segundo):
        print(sum(list(range(primeiro, segundo + 1))))
    else:
        dnv = input('dnv?[N para sair e qualquer tecla para voltar]: ').upper()[0]
        if(dnv == 'N'):
            break