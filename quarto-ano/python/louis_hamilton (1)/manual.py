import sys
import argparse

import matplotlib.pyplot as plt

from hamiltonian import get_queens_possible_attacks, get_hamiltonian, get_qubits_mapping
from data_types import Board, Attacks

def build_board(n:int, attacks:Attacks) -> Board:
    board = []
    for i in range(n):
        board.insert(0,[])
        for j in range(n):
            board[0].append(int((i,j) in attacks))
    return board

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    args = parser.parse_args(sys.argv[1:])

    n = args.n 
    result = get_queens_possible_attacks(n)
    mapping = get_qubits_mapping(n)
    H = get_hamiltonian(n,result,mapping)
    print(H)

    print("---positions---")
    for k,v in result.items():
        print(k,v)

        # board = build_board(n,v)
        # plt.pcolormesh(board, cmap="binary", vmax=1, vmin=0, edgecolors="k",linewidth=2)
        # plt.title(str(k))
        # plt.show()