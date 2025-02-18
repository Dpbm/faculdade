from random import randint
from personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome:str, vida:int, ataque_min:int, ataque_max:int):
        super().__init__(nome, "guerreiro", vida, ataque_min, ataque_max)

    def ataque_especial(self, outro:Personagem):
        """
            Ataque especial: Golpe Poderoso
            +30% de dano + dano extra provido pela arma
        """
        ataque = (self.get_ataque() * 1.3) + self.get_dano_extra()
        outro.vida -= ataque
