dia = int(input('dia>> '))
mes = int(input('mes>> '))
ano = int(input('ano>> '))




bissexto = ((ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0))
((ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0))

a = [(bissexto and (mes < 1  or mes > 12 or dia < 1 or dia > 29)),
     (not(bissexto) and ( mes < 1 or mes > 12 or  dia < 1 or dia > 28))]

print('data valida' if not any(a) else 'data invalida')