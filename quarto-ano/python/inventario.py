import copy

class Item:
    def __init__(self, nome, categoria, efeito, valor):
        self.nome = nome
        self.categoria = categoria
        self.efeito = efeito
        self.valor = valor

    def clone(self):
        """
            Cria um clone do objeto em questão para o uso
            do padrão prototype.
        """

        return copy.deepcopy(self)
    
    def __str__(self):
        return f'nome={self.nome}; categoria={self.categoria}; efeito={self.efeito}; valor={self.valor}'



# Criação dos prototipos
pocao = Item("Poção abrakadabra", "poção", "tontura extrema", 100)
arma = Item("Faca tramontina", "arma", "corte rapido", 60)
armadura = Item("armadura de diamante", "armadura", "a armadura mais resistente da velha guarda", 1000)

# clones
# Além de criar clones, modificaremos todos os atributos (exceto categoria) para cada um deles
# isso será feito para demonstrar que cada clone é um objeto novo independente do prototipo, possuindo apenas os atributos baseados no objeto base
pocao_2 = pocao.clone()
pocao_2.nome = "feitiço do feiticeiro"
pocao_2.efeito = "deixa cego por 3 dias úteis"
pocao_2.valor = 140

arma_2 = arma.clone()
arma_2.nome = "AK45" 
arma_2.efeito = "um hit é fatal" 
arma_2.valor = 8001

armadura_2 = armadura.clone()
armadura_2.nome = "foguinho"
armadura_2.efeito = "relou pega fogo"
armadura_2.valor = 3000

print("Prototipos: ")
print(pocao)
print(arma)
print(armadura)

print("\nClones: ")
print(pocao_2)
print(arma_2)
print(armadura_2)


"""
    Com essa implementação, é extremamente simples criar novos items, principalmente quando são muito parecidos. Aqui, não precisamos 
    inicializar todos os valores na mão, podemos simplesmente criar um item base (protótipo) e se basear nele para a criação de novos items semelhantes,
    sendo assim, se queremos criar duas espadas que apenas diferem em valor, podemos pegar a espada protótipo e alterar apenas o valor:

    ```
        espada = Item("espada", "arma", "ataque forte", 100)
        espada_2 = espada.clone()
        espada_2.valor = 300
    ``` 


    Para jogos de RPG, esse padrão torna-se extremamente útil pra o gerenciamento de inventário. 
    Poderiamos, por exemplo, pensar em um caso em que o jogador encontra um item no chão, sendo este um objeto em memória. 
    Ao realizar a ação de guardar o item em seu invetário, este pode ser clonado para dentro do objeto inventário, 
    assim o jogo não precisará ter o trabalho de criar outro objeto do zero, será necessário apenas fazer uma cópia profunda do item encontrado no cenário,
    uma vez que ambos são o mesmo item.
    Fazendo isso, é muito mais simples de gerenciar objetos no jogo e o código fica muito mais limpo e fácil de ler. 
"""