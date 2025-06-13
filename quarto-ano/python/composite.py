from abc import ABC, abstractmethod

class ComponenteMissao(ABC):
    @abstractmethod
    def executar(self, i=0):
        pass

    @abstractmethod
    def tempo(self):
        pass

    @abstractmethod
    def priorizar(self, index):
        pass

class TarefaSimples(ComponenteMissao):
    def __init__(self, nome, tempo):
        self._nome = nome
        self._tempo = tempo

    def executar(self, i=0):
        pad = " "*i
        print(f"{pad}{i+1}. Executando missao: {self._nome}")

    def tempo(self):
        return self._tempo
    
    def priorizar(self,_):
        pass


class Missao(ComponenteMissao):
    def __init__(self,nome):
        self._nome = nome
        self._filhos = []

    def adicionar(self, componente):
        self._filhos.append(componente)


    def remover(self, componente):
        self._filhos.remove(componente)
        
    def executar(self, i=0):
        pad = " "*i
        print(f"{pad}{i+1}. Executando missao: {self._nome}")
        for filho in self._filhos:
            filho.executar(i+1)
    
    def tempo(self):
        return sum([t.tempo() for t in self._filhos])
    
    def priorizar(self, index):
        component = self._filhos.pop(index)
        self._filhos.insert(0, component)
        

if __name__ == "__main__":
    tarefa1 = TarefaSimples("Lancar foguete", 1)
    tarefa2 = TarefaSimples("Orbitar a lua", 10)
    tarefa3 = TarefaSimples("Coletar amostrar lunares", 3)
    tarefa4 = TarefaSimples("Transmitir dados para a Terra", 4)
    tarefa5 = TarefaSimples("Lancar rover para marte", 12)

    missaoLua = Missao("Missao Lua")
    missaoMarte = Missao("Missao marte")
    missaoPrincipal = Missao("Missao de Exploracao")
    
    missaoLua.adicionar(tarefa1)
    missaoLua.adicionar(tarefa2)
    missaoLua.adicionar(tarefa3)
    missaoLua.adicionar(tarefa4)

    missaoMarte.adicionar(tarefa5)

    missaoPrincipal.adicionar(missaoLua)
    missaoPrincipal.adicionar(missaoMarte)

    missaoPrincipal.priorizar(1)

    missaoPrincipal.executar()


    print(f"tempo para a missao lunar: {missaoLua.tempo()} anos")
    print(f"tempo para a missao marciana: {missaoMarte.tempo()} anos")
    print(f"tempo para a missao principal: {missaoPrincipal.tempo()} anos")