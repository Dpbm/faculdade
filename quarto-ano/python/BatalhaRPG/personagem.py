from abc import ABC, abstractmethod
from random import randint
from arma import Arma

class Personagem(ABC):
    """
        Classe abstrata que implementa todos os elementos base para um personagem
    """

    def __init__(self, nome:str, classe:str, vida:int, ataque_min:int, ataque_max:int):
        self._nome = nome
        self._classe = classe
        self._vida = vida
        self._ataque_min = ataque_min
        self._ataque_max = ataque_max
        self._arma = None

    @property
    def nome(self):
        """
            getter para o atributo nome
        """
        return self._nome
    
    @property
    def classe(self):
        """
            getter para o atributo classe
        """
        return self._classe

    @property
    def ataque_min(self):
        """
            getter para o atributo ataque_min
        """
        return self._ataque_min

    @property
    def ataque_max(self):
        """
            getter para o atributo ataque_max
        """
        return self._ataque_max
    
    @property
    def arma(self):
        """
            getter para o atributo arma
        """
        return self._arma

    @property
    def vida(self):
        """
            getter para o atributo vida
        """
        return self._vida

    @vida.setter
    def vida(self, value:int):
        """
            setter para o atributo vida.

            este é encarregado por não deixar a vida <0
        """
        self._vida = 0 if value < 0 else value

    
    def adicionar_arma(self, nova_arma:Arma):
        """
            Adicionar uma arma ao personagem, garantindo-o dano extra
        """
        self._arma = nova_arma

    def get_ataque(self) -> int:
        """
            Gera um ataque randomico entre ataque_min e ataque_max
        """
        return randint(self._ataque_min, self._ataque_max)

    def get_dano_extra(self) -> int:
        """
            Retorna o dano extra para o ataque
            caso o personagem tenha uma arma
        """
        return 0 if self._arma is None else self._arma.dano_extra

    def atacar(self, outro):
        """
            ataca o oponente (outro) usando o ataque randomico gerado
        """

        ataque = self.get_ataque() + self.get_dano_extra()
        outro.vida -= ataque

    def esta_vivo(self) -> bool:
        """
            verifica se o personagem esta vivo
        """
        return self.vida > 0

    @abstractmethod
    def ataque_especial(self, outro):
        """
            método abstrato usado para adicionar um ataque especial
            para cada classe de personagem derivada da classe base
        """
        pass


    def __str__(self):
        return f"""
        nome: {self._nome}
        classe: {self._classe}
        vida: {self._vida}
        ataque minimo: {self._ataque_min}
        ataque maximo: {self._ataque_max}
        arma: {'Nenhuma' if not self.arma else f'{self.arma.nome} +{self.arma.dano_extra}'}
        """
