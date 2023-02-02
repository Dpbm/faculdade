"""
game Angels and cannibals
https://rachacuca.com.br/jogos/missionarios-e-canibais/
"""

class Game:
    def __init__(self):
        self.right_side = { "angels":3, "cannibals":3 }
        self.left_side  = { "angels":0, "cannibals":0 }
        self.state = "playing"
        self.actual_position = "right"

    def move_left(self, angels, cannibals):
        if(
            angels > self.right_side["angels"] or
            angels > self.right_side["cannibals"] or 
            angels + cannibals > 2 or
            angels + cannibals <= 0 or
            self.actual_position != "right" or
            self.state != "playing"
        ): return "not possible"

        self.left_side["angels"] += angels
        self.left_side["cannibals"] += cannibals
        self.right_side["angels"] -= angels
        self.right_side["cannibals"] -= cannibals
        self.actual_position = "left"

    def move_right(self, angels, cannibals):
        if(
            angels > self.left_side["angels"] or
            angels > self.left_side["cannibals"] or 
            angels + cannibals > 2 or
            angels + cannibals <= 0 or
            self.actual_position != "left" or
            self.state != "playing"
        ): return "not possible"

        self.right_side["angels"] += angels
        self.right_side["cannibals"] += cannibals
        self.left_side["angels"] -= angels
        self.left_side["cannibals"] -= cannibals
        self.actual_position = "right"

    def check_game(self):
        if(self.right_side["angels"] and self.right_side["angels"] < self.right_side["cannibals"]):
            self.state = "lose"
            return
        
        if(self.left_side["angels"] and self.left_side["angels"] < self.left_side["cannibals"]):
            self.state = "lose"
            return

        if(self.left_side["angels"] == 3 and self.left_side["cannibals"] == 3):
            self.state = "win"


class BruteForce:
    def __init__(self):
        self.movements = []
        self.game      = Game()
        #self.possible_boat_states = [(1, 1), (2, 0), (0, 2)]
        self.memo = {}


    def calculate_possibilities(self, position_data):
        possibilities = []

        if(position_data["angels"] == 1):
            possibilities.append((1, 0))

        if(position_data["cannibals"] == 1):
            possibilities.append((0, 1))


        if(position_data["angels"] == 1 and position_data["cannibals"] == 1):
            possibilities.append((1, 1))

        if(position_data["angels"] > 1):
            possibilities.append((2, 0))

        if(position_data["cannibals"] > 1):
            possibilities.append((0, 2))

        return possibilities

    def do_a_try(self, direction):
        from random import choice

        movement = choice(self.possible_boat_states)
        self.movements.append({ "direction":direction, "movement":movement })
        
        return movement
    
    def break_this(self):
        try_count = 0

        while True:
            try_count += 1


            print("-"*10)
            print(f"try #{try_count}")

            angels, cannibals = self.do_a_try("left")
            self.game.move_left(angels, cannibals)
            self.game.check_game()
            print(f"moved left {angels} {cannibals}")

            if(self.game.state == 'lose'):
                print("losed")
                self.game = Game()
                pass

            if(self.game.state == 'win'):
                print("won")
                break

            angels, cannibals = self.do_a_try("right")
            self.game.move_right(angels, cannibals)
            self.game.check_game()
            print(f"moved right {angels} {cannibals}")

            if(self.game.state == 'lose'):
                self.game = Game()
                print("losed")
                pass

            if(self.game.state == 'win'):
                print("won")
                break

b = BruteForce()

b.break_this()

print(b.movements)



        


    