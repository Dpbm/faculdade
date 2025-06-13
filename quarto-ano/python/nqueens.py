from time import sleep

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

    def is_being_attacked_by(self,queen1):
        attackers = []
        for queen2 in self.queens:
            if queen1 == queen2:
                continue


            round_queen1 = [
                (queen1.i, queen1.j+1), 
                (queen1.i, queen1.j-1),
                (queen1.i-1, queen1.j+1),
                (queen1.i-1, queen1.j-1),
                (queen1.i+1, queen1.j+1),
                (queen1.i+1, queen1.j-1),
                (queen1.i-1, queen1.j),
                (queen1.i+1, queen1.j),
            ]

            # get main diagonal
            queen1_main_diagonal = []

            # top portion
            i,j = queen1.pos
            while i > 0:
                i -= 1
                j -= 1
                queen1_main_diagonal.append((i,j))

            # bottom portion
            i,j = queen1.pos
            while i < self.n and j < self.n:
                i += 1
                j += 1
                queen1_main_diagonal.append((i,j))


            # get second diagonal
            queen1_second_diagonal = []

            # top portion
            i,j = queen1.pos
            while i < self.n:
                i += 1
                j += 1
                queen1_second_diagonal.append((i,j))

            # bottom portion
            i,j = queen1.pos
            while i < self.n and j > 0:
                i += 1
                j -= 1
                queen1_second_diagonal.append((i,j))

            
            if(
                queen1.i == queen2.i or 
                queen1.j == queen2.j or
                queen2.pos in round_queen1 or
                queen2.pos in queen1_main_diagonal or
                queen2.pos in queen1_second_diagonal
            ):
                attackers.append(queen1)

        return attackers
    
    def who_is_attacking(self):
        attackers = []
        for queen1 in self.queens:
            tmp = self.is_being_attacked_by(queen1)
            attackers = list(set([*attackers, *tmp]))

        return attackers

    def is_attacking(self):
        return len(self.who_is_attacking()) > 0

    def show(self):
        
        board_str = []
        for i in range(self.n):
            board_str.append([])
            for j in range(self.n):
                board_str[-1].append('-')

        for queen in self.queens:
            board_str[queen.i][queen.j] = 'Q'

        print(board_str)



if __name__ == "__main__":
    board = Board(8)
    board.init_board()

    iteration = 1

    while board.is_attacking():
        print(f"iteracao: {iteration}")

        for queen in board.queens:
            best_pos = queen.pos
            total_attacking = board.is_being_attacked_by(queen)

            for i in range(1,board.n+1):
                queen.move_to((queen.i, (queen.j+i) % board.n))
                
                total_queen_is_being_attacked = board.is_being_attacked_by(queen)
                if(total_queen_is_being_attacked < total_attacking):
                    total_attacking = total_queen_is_being_attacked
                    best_pos = queen.pos

            print(best_pos)
            queen.move_to(best_pos)

        board.show()
        iteration += 1
        sleep(0.6)

