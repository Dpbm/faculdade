class Arma:
    def __init__(self, nome:str, dano_extra:int):
        self._nome = nome
        self._dano_extra = dano_extra

    @property
    def nome(self):
        """
            getter para o atributo nome
        """
        return self._nome

    @property
    def dano_extra(self):
        """
            getter para o atributo dano_extra
        """
        return self._dano_extra
