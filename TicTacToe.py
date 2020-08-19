class Board:

    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False

    def make_turn(self, cell, player):
        if self.is_valid_turn(cell):
            self.state[cell] = player.symbol
            return True
        return False

    def is_full(self):
        for a in self.state:
            if a == 0:
                return False
        print("Tie!")
        return True

    def check_winner(self, player):
        symbol = player.symbol
        if self.state[0] == symbol and self.state[1] == symbol and self.state[2] == symbol:
            return True
        elif self.state[3] == symbol and self.state[4] == symbol and self.state[5] == symbol:
            return True
        elif self.state[6] == symbol and self.state[7] == symbol and self.state[8] == symbol:
            return True
        elif self.state[0] == symbol and self.state[3] == symbol and self.state[6] == symbol:
            return True
        elif self.state[1] == symbol and self.state[4] == symbol and self.state[7] == symbol:
            return True
        elif self.state[2] == symbol and self.state[5] == symbol and self.state[8] == symbol:
            return True
        elif self.state[0] == symbol and self.state[4] == symbol and self.state[8] == symbol:
            return True
        elif self.state[2] == symbol and self.state[4] == symbol and self.state[6] == symbol:
            return True

    def convert_zero(self, num):
        if num == 0:
            return " "
        elif num == 1:
            return "X"
        else:
            return "O"

    def print_board(self):
        print(" " + self.convert_zero(self.state[0]) + " | " + self.convert_zero(
            self.state[1]) + " | " + self.convert_zero(self.state[2]) + " ")
        print(" " + self.convert_zero(self.state[3]) + " | " + self.convert_zero(
            self.state[4]) + " | " + self.convert_zero(self.state[5]) + " ")
        print(" " + self.convert_zero(self.state[6]) + " | " + self.convert_zero(
            self.state[7]) + " | " + self.convert_zero(self.state[8]) + " ")


#  inst = Board()
#  inst.print_board()

class Player:

    def __init__(self, symbol):
        self.symbol = symbol


if __name__ == '__main__':
    player_a = Player(1)
    player_b = Player(-1)
    board = Board()
    active_player = player_a

    while not board.is_full():
        board.print_board()
        try:
            cell = int(input("Where do you want to place your sign? [1 - 9]"))
        except ValueError:
            continue
        cell = cell - 1
        if cell < 0 or cell > 8:
            print("Please enter a number between 1 and 9")
            continue
        if not board.make_turn(cell, active_player):
            print("Invalid move. Try again!")
            continue
        if board.check_winner(active_player):
            print("You have won the game!!!")
            print("Congratulation!")
            break
        if active_player == player_a:
            active_player = player_b
        else:
            active_player = player_a

# vielleicht gegen KI?
