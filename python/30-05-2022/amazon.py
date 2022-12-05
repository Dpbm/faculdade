class Map:
    def __init__(self, i, j):
        self.map = [ ['.' for _ in range(20)] for _ in range(20)]
        self.map[i][j] = '+'
        self.i = i
        self.j = j
        self.commands = {
                "N": self.go_north,
                "L": self.go_east,
                "O": self.go_west,
            }

    def go_north(self, steps):
        for _ in range(int(steps)):
            self.fix_inifinite_map()
            self.i -= 1
            self.map[self.i][self.j] = '+'

    def go_east(self, steps):
        for _ in range(int(steps)):
            self.fix_inifinite_map()
            self.j += 1
            self.map[self.i][self.j] = '+'

    def go_west(self, steps):
        for _ in range(int(steps)):
            self.fix_inifinite_map()
            self.j -= 1
            self.map[self.i][self.j] = '+'

    def tree(self):
        self.map[self.i][self.j] = '#'
    
    def show_matrix(self):
        for row in self.map:
            for element in row:
                print(element, end=' ')
            print()

        exit()

    def fix_inifinite_map(self):
        if(self.i - 1 <= -20 or self.j - 1 <= -20):
            self.i = 0

        if(self.j + 1 >= 20 or self.j + 1 >= 20):
            self.j = 0

class AmazonGame:
    def __init__(self, i, j):
        self.map = Map(i, j)
        self.state = True

    def get_input(self):
        input_command_parameter = input().split()
    
        if input_command_parameter[0] == 'S':
            self.state = False
            return

        if input_command_parameter[0] == 'A':
            self.map.tree()
            return


        command, parameter = input_command_parameter

        self.map.commands[command](parameter)

    def play(self):
        if not self.state:
            self.map.show_matrix() 

        self.get_input()
        self.play()

i, j = [int(i) for i in input().split()]

game = AmazonGame(i, j)
game.play()



