from time import sleep
import matplotlib.pyplot as plt

class Queen:
    def __init__(self, pos):
        self.pos = pos

    @property
    def i(self):
        return self.pos[0]
    
    @property
    def j(self):
        return self.pos[1]

    def move_to(self,pos):
        self.pos=pos

class Board:
    def __init__(self, n):
        self.board = []
        self.queens = []
        self.n = n
    
    def init_board(self):
        for i in range(self.n):
            self.board.append([])
            for j in range(self.n):
                if j == 0:
                    queen = Queen((i,j))
                    self.queens.append(queen)
                    self.board[-1].append(queen)
                else:
                    self.board[-1].append(None)

    def is_q1_attacking_q2(self,q1, q2):
        if q1 == q2:
            return False
        
        round_q1 = [
            (q1.i, q1.j+1), 
            (q1.i, q1.j-1),
            (q1.i-1, q1.j+1),
            (q1.i-1, q1.j-1),
            (q1.i+1, q1.j+1),
            (q1.i+1, q1.j-1),
            (q1.i-1, q1.j),
            (q1.i+1, q1.j),
        ]

        # get main diagonal
        q1_main_diagonal = []

        # top portion
        i,j = q1.pos
        while i > 0:
            i -= 1
            j -= 1
            q1_main_diagonal.append((i,j))

        # bottom portion
        i,j = q1.pos
        while i < self.n and j < self.n:
            i += 1
            j += 1
            q1_main_diagonal.append((i,j))


        # get second diagonal
        q1_second_diagonal = []

        # top portion
        i,j = q1.pos
        while i < self.n:
            i += 1
            j += 1
            q1_second_diagonal.append((i,j))

        # bottom portion
        i,j = q1.pos
        while i < self.n and j > 0:
            i += 1
            j -= 1
            q1_second_diagonal.append((i,j))

        

        return (
            q1.i == q2.i or 
            q1.j == q2.j or
            q2.pos in round_q1 or
            q2.pos in q1_main_diagonal or
            q2.pos in q1_second_diagonal
        )
    

    def q1_is_attacking_who(self,q1):
        attacking = []
        for q2 in self.queens:
            if(self.is_q1_attacking_q2(q1,q2)):
                attacking.append(q2)
        return attacking
    
    def q1_is_being_attacked_by_who(self,q1):
        attackers = []
        for q2 in self.queens:
            if(self.is_q1_attacking_q2(q2,q1)):
                attackers.append(q2)
        return attackers
    
    def has_attacks(self):
        attacks = []
        for q in self.queens:
            tmp = self.q1_is_attacking_who(q)
            attacks = list(set([*attacks, *tmp]))
        return len(attacks) > 0
    
    def move_queen_right(self,queen):
        queen.pos = (queen.i, (queen.j + 1)%self.n)

    def show(self):
        board = []
        for _ in range(self.n):
            board.append([])
            for _ in range(self.n):
                board[-1].append(0)

        for queen in self.queens:
            board[queen.i][queen.j] = 1

        plt.pcolormesh(board,edgecolors="k",linewidth=2)
        plt.savefig(f"solution-{self.n}-queens.png", bbox_inches="tight", dpi=300)
        plt.show()


if __name__ == "__main__":
    board = Board(15)
    board.init_board()

    iteration = 1
    solutions = []

    get_score = lambda queen: len(board.q1_is_attacking_who(queen)) + len(board.q1_is_being_attacked_by_who(queen))

    while board.has_attacks():
        print(f"iteracao: {iteration}")

        for queen_i, queen in enumerate(board.queens):
            best_score = get_score(queen)
            best_pos = queen.pos

            for _ in range(0, board.n):
                board.move_queen_right(queen)

                new_score = get_score(queen)

                if new_score < best_score:
                    best_score = new_score
                    best_pos = queen.pos

            if best_score != 0:
                board.move_queen_right(queen)
            else:
                queen.pos = best_pos

            print(f"score{queen_i}: {best_score}", end=" ")

        iteration += 1

    board.show()
