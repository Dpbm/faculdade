from random import randint
from personagem import Personagem

class Arqueiro(Personagem):
    def __init__(self, nome:str, vida:int, ataque_min:int, ataque_max:int):
        super().__init__(nome, "arqueiro", vida, ataque_min, ataque_max)

    def ataque_especial(self, outro:Personagem):
        """
            Ataque especial: Flecha dupla
            dois ataques menores + dano extra da arma
        """
        ataque = (self.ataque_min * 2) + self.get_dano_extra()
        outro.vida -= ataque
