

class Connect_four:
    """ This class represents the game connect four"""

    def __init__(self):
        self._board = [['' for spot in range(7)] for spot in range(6)]
        self._player = 'x'
        self._game_state = 'UNFINISHED'

    def get_player(self):
        return self._player

    def get_game_state(self):
        return self._game_state

    def print_game_state(self):
        print(self._game_state)
        return

    def print_board(self):
        print('col: 0   1   2   3   4   5   6')
        for row in reversed(self._board):
            print('   '+ str(row))



    def make_move(self, col):

        # stops when the game is finished
        if self._game_state != 'UNFINISHED':
            return False

       # test if its in bound
        elif col < 0 or col > 6:
            return False


        for row in range(6):
            if self._board[row][col] == '':
                self._board[row][col] = self.get_player()
                self.horizontal_win(row, col)
                self.vertical_win(row, col)
                self.negative_diagonals_win(row, col)
                self.positive_diagonals_win(row, col)
                self.check_draw()

                return True

        # in case they move where it is filled up in a column, they don't lose a turn
        if self._board[5][col] != '':
            return False



    def check_draw(self):
        """ check for draws"""
        count = 0
        for col in range(7):
            if self._board[-1][col] != '':
                count += 1

        if count == 7:
            self._game_state = 'DRAW'
            return self.get_game_state()

    # change the player
    def change_player(self, player):
        """ changes the player """
        if player == 'x':
            self._player = 'o'
            return True

        else:
            self._player = 'x'
            return True

    def horizontal_win(self,row, col):
        count = 1
        for num in range(1,4):

            if col - num < 0:
                break

            elif self._board[row][col - num] != self._player:
                break

            if self._board[row][col - num] == self._player:
                print('C')
                count += 1

        for num in range(1,4):

            if col + num > 6:
                break

            elif self._board[row][col + num] != self._player:
                break

            elif self._board[row][col + num] == self._player:
                count += 1

        if count >= 4:
            self._game_state = "{} WON".format(self._player)

    def vertical_win(self, row, col):
        """ Checks for vertical wins """
        count = 1
        for num in range(1,4):

            if row - num < 0:
                break

            elif self._board[row - num][col] != self._player:
                break

            elif row - num < 0:
                break

            elif self._board[row - num][col] == self._player:
                count += 1

        if count >= 4:
            self._game_state = "{} WON".format(self._player)


    def negative_diagonals_win(self,row, col):
        count = 1
        for num in range(1,4):

            if col - num < 0 or col - num < 0:
                break

            elif self._board[row - num][col - num] != self._player:
                break


            elif self._board[row - num][col - num] == self._player:
                count += 1

        for num in range(1,4):

            if row + num > 5 or col + num > 6:
                break

            elif self._board[row + num][col + num] != self._player:
                break

            elif self._board[row + num][col + num] == self._player:
                count += 1

        if count >= 4:
            self._game_state = "{} WON".format(self._player)

    def positive_diagonals_win(self,row, col):
        count = 1
        for num in range(1,4):

            if row - num < 0 or col + num > 5:
                break

            elif self._board[row - num][col + num] != self._player:
                break

            elif self._board[row - num][col + num] == self._player:
                count += 1

        for num in range(1,4):

            if row + num > 5 or col - num < 0:
                break

            elif self._board[row + num][col - num] != self._player:
                break

            elif self._board[row + num][col - num] == self._player:
                count += 1

        if count >= 4:
            self._game_state = "{} WON".format(self._player)

if __name__ == '__main__':
    c4 = Connect_four()



    while c4.get_game_state() == 'UNFINISHED':
        c4.print_board()
        print('PLAYER {}'.format(c4.get_player()))
        col = int(input('Enter Col: '))

        if c4.make_move(col):
            c4.change_player(c4.get_player())


    if c4.get_game_state() != 'UNFINISHED: ':
        c4.print_board()
        print(c4.get_game_state())

