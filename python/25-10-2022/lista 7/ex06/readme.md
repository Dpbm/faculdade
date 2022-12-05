# Problema das Lâmpadas
Você  está  de  volta  em  seu  hotel  na  Tailândia  depois  de  um  dia  de  mergulhos.  O  seu  quarto  tem  duas lâmpadas.  Vamos  chamá-las  de  A  e  B.  No  hotel  há  dois  interruptores,  que  chamaremos  de  I1e  I2.  Ao apertar I1, a lâmpada A troca de estado, ou seja, acende se estiver apagada e apaga se estiver acesa. Se apertar I2, ambas as lâmpadas A e B trocam de estado. As lâmpadas inicialmente estão ambas apagadas. Seu amigo resolveu bolar um desafio para você. Ele irá apertar os interruptores em uma certa sequência, e gostaria que você respondesse o estado final das lâmpadas A e B.

## Entrada
A  primeira  linha  contém  um  número  N  que  representa  quantas  vezes  seu  amigo  irá  apertar  algum interruptor. Na linha seguinte seguirão N números, que pode ser 1, se o interruptor I1foi apertado, ou 2, se o interruptor I2foi apertado.

## Saída
Seu programa deve imprimir dois valores, em linhas separadas. Na primeira linha, imprima 1 se a lâmpada A estiver acesa no final das operações  e 0 caso contrário. Na segunda linha, imprima  1 se a lâmpada B estiver acesa no final das operações e 0 caso contrário.

## Restrições
1 ≤ N ≤ 105


# Adicionais
Para complementar este problema e ajudar a gente a enteder como mexer com arquivos em python, foi dada a seguinte questão:

Para montar uma maratona de  programação é  necessário criar para cada problema os arquivos de entrada e os arquivos de saída. Para cada entrada deve que ser criado n arquivos de entrada em uma pasta input, com os nomes A_1, A_2, A_3,.., A_n, executados com a solução do problema gerando n arquivos de saída em uma pasta output, com os nomes A_1, A_2, A_3, ..., A_n.

Faça um programa em Pyhton que gere 100 arquivos de entrada e de saída para o problema abaixo.

Com isso, resolvi utilizar dos meus conhecimentos e fazer uma espécie de mapeamento de todas as entradas e saídas possíveis. No entanto fui descuidado e esqueci que as entradas iam de `1 à 105` e os valores de entrada podiam ser `1 ou 2`, ou seja, a quantidade de combinações é de `2 ^ 105 = 4.0564819e+31`, ou seja coisa pra caramba para rodar em um computador convencional, criando bilhares de bilhares de arquivos em sequência, sem nenhuma pausa.

## Sendo assim, ao rodar esse programa, utilize um range menor que `range(1, 106)` se não provavelmente seu sistema vai travar ou ficar muito lento
