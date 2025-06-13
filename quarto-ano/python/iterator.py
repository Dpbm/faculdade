
class Produto:
    # Define o objeto produto com seus dados internos
    def __init__(self, id, nome, preco):
        self._id = id
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return f"[{self._id}] {self._nome} está por {self._preco}"

class ColecaoProdutos:
    # Define a class que controlará a coleção de produtos
    # nesse caso, a classe é responsável por salvar os produtos e
    # retornar um iterator quando requisitado
    def __init__(self,reverso=False):
        self.produtos = []
        self._reverse = reverso

    def adicionar_produto(self,produto):
        self.produtos.append(produto)

    def total_produtos(self):
        return len(self.produtos)
    
    def __iter__(self):
        # retorna um iterator para ser usado em 
        # loops
        return IteradorProdutos(self, self._reverse)
    

class IteradorProdutos:
    # define o iterator de produtos
    # a cada iteração um produto é devolvido para o usuário
    # podemos usar tanto a ordem direta como inversa
    def __init__(self,colecao, reverse):
        self._colecao = colecao
        self._total = colecao.total_produtos() 


        #define variaveis de controle
        # 
        # deve o index inicial sendo -1 na ordem direta e o tamanho da colecao na ordem inversa    
        # essa escolha se da pois antes de retornar o produto, atualizamos o index
        self._index = -1 if not reverse else self._total
        # define o limite das iterações, sendo o total de items -1 o valor para a ordem direta
        # e 0 o valor para a ordem inversa, ja que estamos inicializando o index com um valor a mais
        self._limit = self._total-1 if not reverse else 0
        # define o passo que o index deve ser incrementado ou decrementado
        self._step = 1 if not reverse else -1

    def __next__(self):
        # devolve o proximo valor da coleção
        if self._index == self._limit:
            raise StopIteration

        self._index += self._step
        return self._colecao.produtos[self._index]
    
if __name__ == "__main__":
    colecao = ColecaoProdutos()
    colecao.adicionar_produto(Produto(1, "test1", 10.5))
    colecao.adicionar_produto(Produto(2, "test2", 3.5))
    colecao.adicionar_produto(Produto(3, "test3", 40.5))
    colecao.adicionar_produto(Produto(4, "test4", 3.3))
    colecao.adicionar_produto(Produto(5, "test67", 3.3))

    print("--Ordem Direta--")
    for produto in colecao:
        print(produto)

    #----------------------------------------------------------

    colecao = ColecaoProdutos(reverso=True)
    colecao.adicionar_produto(Produto(1, "test1", 10.5))
    colecao.adicionar_produto(Produto(2, "test2", 3.5))
    colecao.adicionar_produto(Produto(3, "test3", 40.5))
    colecao.adicionar_produto(Produto(4, "test4", 3.3))
    colecao.adicionar_produto(Produto(5, "test67", 3.3))

    print("--Ordem Reversa--")
    for produto in colecao:
        print(produto)


"""
O padrão iterator é extremamente util neste caso, pois precisamos acessar items sequencialmente
sem a necessidade de saber como os dados estão armazenados internamente.

Neste padrão, os dados são armazenados internamente no objeto, e a cada iteração, o objeto é responsável
por manipular os dados salvos e dizer qual é o próximo a ser pego na coleção.
"""