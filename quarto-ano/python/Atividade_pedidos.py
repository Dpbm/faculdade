from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def exibir_informacoes():
        pass

    @abstractmethod
    def adicionar_ao_pedido():
        pass


class Eletronico(Produto):
    def __init__(self, modelo:str, preco:float):
        self._modelo = modelo
        self._preco = preco

    def exibir_informacoes(self):
        print(f"""
            Eletronico: {self._modelo}
            Preço: {self._preco:.2f}
        """)

    def adicionar_ao_pedido(self):
        print(f"{self._modelo} adicionado ao pedido")



class Roupa(Produto):
    def __init__(self, tipo:str, preco:float):
        self._tipo = tipo
        self._preco = preco

    def exibir_informacoes(self):
        print(f"""
            Roupa: {self._tipo}
            Preço: {self._preco:.2f}
        """)

    def adicionar_ao_pedido(self):
        print(f"{self._tipo} adicionado ao pedido")



class Alimento(Produto):
    def __init__(self, nome:str, preco:float):
        self._nome = nome
        self._preco = preco

    def exibir_informacoes(self):
        print(f"""
            Alimento: {self._nome}
            Preço: {self._preco:.2f}
        """)

    def adicionar_ao_pedido(self):
        print(f"{self._nome} adicionado ao pedido")



class ProdutoFactory:
    @staticmethod
    def criar_produto(tipo:str, info:str, preco:float) -> Produto: 
        tipos = ["eletronico", "roupa", "alimento"]
        classes = [Eletronico, Roupa, Alimento]
        produtos = { tipo:classe for tipo,classe in zip(tipos, classes) }

        if(not tipo in tipos):
            raise Exception("Tipo de produto invalido!")
        
        produto_class = produtos[tipo]

        return produto_class(info, preco)


if __name__ == "__main__":
    factory = ProdutoFactory()

    pedidos = [
        {"tipo":"eletronico", "info":"Iphone XR", "preco":1000000000.0},
        {"tipo":"roupa", "info":"Camiseta XGG", "preco":7500.0},
        {"tipo":"alimento", "info":"Linguiça Berssane", "preco":30.5},
        {"tipo":"roupa", "info":"Short Jeans", "preco":190.0},
        {"tipo":"alimento", "info":"Farofa", "preco":10.6}
    ]

    print("===Pedidos===")

    for pedido in pedidos:
        print("-"*30)
        produto = factory.criar_produto(pedido["tipo"], pedido["info"], pedido["preco"])
        produto.exibir_informacoes()
        produto.adicionar_ao_pedido()


        

