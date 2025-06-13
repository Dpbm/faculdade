class Luz:
    def ligar(self):
        print("A luz está ligada.")

    def desligar(self):
        print("A luz está desligada.")

    def intensidade(self, intensidade):
        print(f"A intensidade da luz esta em: {intensidade}")

class Comando:
    def executar(self):
        pass

class ComandoLigarLuz(Comando):
    def __init__(self, luz):
        self.luz = luz

    def executar(self):
        self.luz.ligar()

class ComandoDesligarLuz(Comando):
    def __init__(self, luz):
        self.luz = luz

    def executar(self):
        self.luz.desligar()

class ComandoDimmer(Comando):
    def __init__(self, luz, intensidade):
        self.luz = luz
        assert intensidade <= 100 and intensidade >= 0, "intensidade invalid (valores devem estar entre 0 e 100)"
        self.intensidade = intensidade

    def executar(self):
        self.luz.intensidade(self.intensidade)

class ControleRemoto:
    def __init__(self):
        self._comando = None

    def definir_comando(self, comando):
        self._comando = comando

    def pressionar_botao(self):
        if self._comando:
            self._comando.executar()

if __name__ == "__main__":
    luz = Luz() 
    comando_ligar = ComandoLigarLuz(luz)
    comando_desligar = ComandoDesligarLuz(luz)
    comando_dimmer = ComandoDimmer(luz, 10)

    controle = ControleRemoto()

    controle.definir_comando(comando_ligar)
    controle.pressionar_botao()

    controle.definir_comando(comando_desligar)
    controle.pressionar_botao()

    controle.definir_comando(comando_dimmer)
    controle.pressionar_botao()