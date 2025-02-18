from random import randint
from personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome:str, vida:int, ataque_min:int, ataque_max:int):
        super().__init__(nome, "mago", vida, ataque_min, ataque_max)

    def ataque_especial(self, outro:Personagem):
        """
            Ataque especial: Bola de fogo
            Pelo requisito estava escrito ignorar defesa
            como defesa nao foi requisitado, interpretei como 
            dano máximo + dano extra provido pela arma
        """
        ataque = self.ataque_max + self.get_dano_extra()
        outro.vida -= ataque

