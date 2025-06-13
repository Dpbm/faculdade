from typing import Dict, Tuple, List

N = 4
MAX_I = N-1

Position = Tuple[int,int]
MappingQubits = Dict[Position, int]
Attacks = List[Position]
MappingAttacks = Dict[Position, Attacks]


def get_qubits_mapping(n:int) -> MappingQubits:
    qubits_mapping = {}
    qubit = 0
    for i in range(n):
        for j in range(n):
            qubits_mapping[(i,j)] = qubit
            qubit += 1
    return qubits_mapping

def get_queens_possible_attacks(n:int) -> MappingAttacks:
    attacks = {}

    for i in range(n):
        for j in range(n):
            pos = (i,j)

            attacks[pos] = []
            attacks[pos].append(pos)

            cols = [(next_i, j) for next_i in range(N) if next_i != i] # same coloumn
            rows = [(i, next_j) for next_j in range(N) if next_j != j] # same row

            for c,r in zip(cols,rows):
                attacks[pos].append(c)
                attacks[pos].append(r)


            first_row = i
            # if the current column is 0, so we have no top diagonal
            # the same happens for row == 0
            if i > 0 and j > 0:
                first_row = (i - j) if j < i else 0

            last_row = (N - j - 1) + 1
            if last_row > MAX_I:
                last_row = MAX_I

            for row in range(first_row, last_row):
                if row == i:
                    continue

                col = j - row
                attacks[pos].append((row,col))


    return attacks            





