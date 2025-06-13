import copy

class Inimigo:
    def __init__(self, tipo, nivel, pontos_vida):
        self.tipo = tipo
        self.nivel = nivel
        self.pontos_vida = pontos_vida

    def clone(self):
        """
        cria um clone da classe contendo os mesmo dados da classe base
        """
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"tipo={self.tipo}; nivel={self.nivel}; vida={self.pontos_vida}"
    

# cria inimigos base de cada tipo para a criação dos clones
orc = Inimigo("Orc", 10, 100)
troll = Inimigo("Troll", 20, 80)
goblin = Inimigo("Goblin", 5, 50)

# criam-se 3 clones dos quais serão modificados
orc_clone = orc.clone()
troll_clone = troll.clone()
goblin_clone = goblin.clone()

"""
após a clonagem, foram modificados os parametros de cada clone. Aqui foi modificado apenas um parâmetro
de orc e troll e ambos os paramêtros para o clone do goblin, demonstrando que as classes clonadas são 
objetos distintos.
"""
orc_clone.pontos_vida = 200
troll_clone.nivel = 100
goblin_clone.pontos_vida = 120
goblin_clone.nivel = 30

print("Inimigos base: ")
print(orc)
print(troll)
print(goblin)
print("Clones: ")
print(orc_clone)
print(troll_clone)
print(goblin_clone)

"""
Nesse código, o padrão prototype é muito útil pois, evita a criação de novas instâncias de classes sem necessidade, uma vez que todo orc teria os mesmo atributos do primeiro orc criado. Aqui, poderiamos criar dezenas de Trolls, por exemplo, sem a necessidade de especificar multiplas vezes seus atributos, modificando-os apenas quando necessário.
"""
