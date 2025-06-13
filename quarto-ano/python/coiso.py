from abc import ABC, abstractmethod

# Interface Componente
class Componente(ABC):
    @abstractmethod
    def mostrar_detalhes(self, nivel=0):
        pass



# Classe Tarefa (Cartão)
class Tarefa(Componente):
    def __init__(self, descricao, prioridade, duracao, responsavel):
        self.descricao = descricao
        self.prioridade = prioridade
        self.duracao = duracao
        self.responsavel = responsavel

    def mostrar_detalhes(self, nivel=0):
        prefixo = " " * (nivel * 2)
        print(f"{prefixo}Tarefa: {self.descricao}, Prioridade: {self.prioridade}, Duração: {self.duracao}h, Responsável: {self.responsavel}")


# Classe Lista de Tarefas (Lista)
class ListaTarefas(Componente):
    def __init__(self, titulo):
        self.titulo = titulo
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def remover(self, tarefa):
        self.tarefas.remove(tarefa)

    def mostrar_detalhes(self, nivel=0):
        prefixo = " " * (nivel * 2)
        print(f"{prefixo}Lista: {self.titulo}")
        for tarefa in self.tarefas:
            tarefa.mostrar_detalhes(nivel + 1)


# Classe Projeto (Quadro)
class Projeto(Componente):
    def __init__(self, titulo):
        self.titulo = titulo
        self.listas = []

    def adicionar(self, lista):
        self.listas.append(lista)

    def remover(self, lista):
        self.listas.remove(lista)

    def mostrar_detalhes(self, nivel=0):
        prefixo = " " * (nivel * 2)
        print(f"{prefixo}Projeto: {self.titulo}")
        for lista in self.listas:
            lista.mostrar_detalhes(nivel + 1)

if __name__ == "__main__":
    # Criando tarefas
    tarefa1 = Tarefa("Implementar login", "Alta", 5, "João")
    tarefa2 = Tarefa("Criar banco de dados", "Média", 8, "Maria")
    tarefa3 = Tarefa("Desenvolver frontend", "Baixa", 12, "Carlos")

    # Criando listas de tarefas
    lista1 = ListaTarefas("Backlog")
    lista2 = ListaTarefas("Em Andamento")
    lista3 = ListaTarefas("Concluído")

    # Adicionando tarefas às listas
    lista1.adicionar(tarefa1)
    lista1.adicionar(tarefa2)
    lista2.adicionar(tarefa3)

    # Criando projeto (quadro)
    projeto = Projeto("Projeto Kanban")
    projeto.adicionar(lista1)
    projeto.adicionar(lista2)
    projeto.adicionar(lista3)

    #lista1.remover(tarefa2)


    # Mostrando detalhes do projeto
    projeto.mostrar_detalhes()
