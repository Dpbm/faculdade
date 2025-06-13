import random
from math import sqrt
from copy import deepcopy
from typing import List, Tuple
import numpy as np

Row = np.array
Column = np.array
Square = np.array
BoardData = np.array
Coordinates = Tuple[int, int]

MAX_RANDOM_PER_ROW = 4
MIN_VALUE_PER_CELL = 1
MAX_VALUE_PER_CELL = 9
MUTATION_RATE = 0.06

class Board:
    def __init__(self, n:int=9):
        self._n = n
        self._side = sqrt(self._n)
        self._board = np.zeros(shape=(self._n, self._n), dtype=np.int8)
        self._empty_positions = []

        self._randomize_board()
        self._save_empty_pos()

    def _get_column(self, j:int) -> Column:
        return self._board[:, j]
    
    def _get_row(self, i:int) -> Row:
        return self._board[i]

    def _get_random_number(self,min_val:int=MIN_VALUE_PER_CELL, max_val:int=MAX_VALUE_PER_CELL) -> int:
        return random.randint(min_val,max_val)

    def _should_add_random_number(self) -> bool:
        return bool(random.randint(0,1))

    def _get_square_pos(self, i:int) -> int:
        return i//self._side

    def set_at_pos(self,i:int, j:int, value:int):
        self._board[i][j] = value

    def _is_in_the_same_square(self, base:Coordinates, current:Coordinates) -> bool:
        base_i, base_j = base
        current_i, current_j = current

        return self._get_square_pos(base_i) == self._get_square_pos(current_i) and self._get_square_pos(base_j) == self._get_square_pos(current_j)

    def _get_min_square(self, i:int, j:int) -> Square:
        values = []
        for row in range(self._n):
            for column in range(self._n):
                if(self._is_in_the_same_square((i,j),(row,column))):
                    values.append(self._board[row][column])
        return np.array(values, dtype=np.int8)


    def _randomize_board(self):
        for row in range(self._n):
            total_in_row = 0
            for column in range(self._n):
                get_random_number = self._should_add_random_number()

                if total_in_row >= MAX_RANDOM_PER_ROW:
                    break

                if not get_random_number:
                    continue

                while True:
                    random_numer = self._get_random_number()
                    if (self.is_a_valid_move(row, column, random_numer)):
                        self.set_at_pos(row, column, random_numer)
                        break

                total_in_row += 1
    
    def is_a_valid_move(self, i:int, j:int, number:int) -> bool:
        # it's pretty slow, but for now, it works
        column_values = self._get_column(j)
        row_values = self._get_row(i)
        square_values = self._get_min_square(i,j)
        return not number in np.concatenate((column_values, row_values, square_values), axis=None)

    @property
    def board(self) -> BoardData:
        return self._board

    @property
    def total_empty(self) -> int:
        return len(self._empty_positions)

    @property
    def empty_positions(self) -> List[Coordinates]:
        return self._empty_positions

    def _save_empty_pos(self):
        for i in range(self._n):
            for j in range(self._n):
                if(self._board[i][j] == 0):
                    self._empty_positions.append((i,j))
    
    @property
    def n(self) -> int:
        return self._n

    def show(self):
        print(" " + "-"*28) 
        for i in range(self._n):
            for j in range(self._n):
                if j%3 == 0:
                    print(" | ",end="")
                print(self._board[i][j], end=" ")

            print(" | ")
            if i > 0 and (i+1) % 3 == 0 :
                print(" " + "-"*28) 

class Gene:
    def __init__(self, min_range:int=MIN_VALUE_PER_CELL, max_range=MAX_VALUE_PER_CELL):
        self._min_range = min_range
        self._max_range = max_range
        self._value = random.randint(min_range, max_range)
    
    def mutate(self, rate:float=MUTATION_RATE):
        if random.random() > rate:
            return

        self._value = random.randint(self._min_range, self._max_range)

    @property
    def value(self) -> int:
        return self._value

class Chromossome:
    def __init__(self,size:int):
        self._i = 0
        self._max = size
        self._genes = [Gene() for _ in range(size)]

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= self._max:
            raise StopIteration

        gene = self._genes[self._i]
        self._i += 1

        return gene
    
    def __str__(self) -> str:
        return "[" + ", ".join([str(gene.value) for gene in self._genes]) + "]"

class Agent:
    def __init__(self, board:Board):
        self._board = board
        self._ch = Chromossome(board.total_empty)
    
    def _setup_solution_board(self):
        for gene,pos in zip(self._ch, self._board.empty_positions):
            print(pos, gene.value)
            i,j = pos
            self._board.set_at_pos(i,j,gene.value)

    def performance(self,base_board:Board):
        self._setup_solution_board()
        return self._board.board - base_board.board

    @property
    def board(self)  -> Board:
        return self._board

    @property
    def chromossome(self) ->Chromossome:
        return self._ch

class Population:
    def __init__(self, amount:int, board:Board):
        self._individuals = [Agent(deepcopy(board)) for _ in range(amount)]
        self._best_board = deepcopy(board)

    def show(self):
        for ind in self._individuals:
            print(ind.chromossome)

if __name__ == "__main__":
    board = Board()
    board.show()

    a = Agent(deepcopy(board))

    a.board.show()

    print(a.performance(board))



    # TODOS
    # 1. dar uma pontuação pro tabuleiro (numpy)
    # 2. selecionar os individuos
    # 3. fazer crossover
    # 4. nova geração
    





    