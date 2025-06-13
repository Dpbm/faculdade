# -*- coding: utf-8 -*-

class Piece:
    """Flyweight que representa a parte compartilhada de uma peça."""

    """
        Essa classe será nosso Flyweight, uma vez color seria usado muitas vezes
        por diversos objetos, o que seria desnecessário, e um gasto a mais de memória.
        Sendo assim, color é seu estado intrínseco.
    """
    def __init__(self, color):
        self.color = color  # Cor é estado intrínseco

    def __str__(self):
        return f"P-{self.color[0].upper()}"

class PieceFactory:
    """Fábrica que gerencia instâncias de Piece (Flyweights)."""
    _pieces = {}

    """
        Para facilitar a criação das peças. Podemos criar uma fabrica
        que possui salvo as instâncias de peças já criadas. Dessa forma
        apenas objetos com cores não existentes serão criados e armazenados na memória, 
        economizando espaço. 
    """
    @classmethod
    def get_piece(cls, color):
        if color not in cls._pieces:
            cls._pieces[color] = Piece(color)
        return cls._pieces[color]

class PieceInstance:
    """Instância concreta de uma peça em uma posição, com estado extrínseco."""

    """
    Aqui criamos uma classe context que receberá um flyweight (a referência em memória).
    Com isso, usaremos um objeto compartilhado e adicionaremos lógica em cima disso.
    """
    def __init__(self, flyweight_piece, is_king=False):
        self.flyweight = flyweight_piece  # Referência ao flyweight
        self.is_king = is_king  # Estado extrínseco

    def make_king(self):
        self.is_king = True

    def __str__(self):
        return f"{'K' if self.is_king else str(self.flyweight)}"

class Board:
    """Tabuleiro com instâncias de peças, cada uma contendo seu estado próprio."""
    
    """
        Criamos então uma classe cliente que utiliza a classe flyweight e passa
        as instancias para a classe context. 
        Nesse caso, temos um tabuleiro de damas, utilizando as peças únicas criadas,
        e gerenciando quando uma ou outra deve ser usada.
    """

    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
    

    def setup_pieces(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    """
                        Aqui, uma lógica é usada para saber qual objeto deve ser usado, sendo a fábrica responsável por pegar
                        ou criar o objeto requisitado. Após isso, passamos a instância para a classe context.
                        Assim, em meória teremos apenas dois objetos no total, mas aqui eles são usados diversas vezes
                        e seus valores extrínsecos gerenciados pela classe cliente e passados para a context.
                    """
                    if i < 3:
                        piece = PieceFactory.get_piece('black')
                        self.grid[i][j] = PieceInstance(piece)
                    elif i > 4:
                        piece = PieceFactory.get_piece('white')
                        self.grid[i][j] = PieceInstance(piece)

    def draw_board(self):
        for row in self.grid:
            print(' '.join(str(p) if p else '.' for p in row))
        print()

class Game:
    def __init__(self):
        self.board = Board()

    def start(self):
        self.board.draw_board()

# Iniciar jogo
game = Game()
game.start()

"""
    Executando o game, podemos ver que todas as peças foram colocadas no tabuleiro corretamente.
    Mas em memória, conseguimos economizar muito espaço, usando 2 objetos apenas ao invés de 24.
"""

print(PieceFactory._pieces) # apenas duas peças