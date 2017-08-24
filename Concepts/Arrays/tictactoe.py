class TicTacToe(object):
    '''A Tac tac toe game'''
    def __init__(self):
        '''Start a new game'''
        self._board = [[None, None, None], [None, None, None], [None, None, None]] #Create an empty board
        self._player = 'X'

    def mark(self, i, j):
        '''Put an X or O at position i,j'''
        print(i,j)
        if not (0 <= i <= 2 and 0 <= j <= 2):                       #Check if the index values are between 0 and 2
            raise ValueError('Index i and j are out of Range')
        if self._board[i][j] != None:                             #Check if the index values is empty
            raise ValueError('Position is already filled')
        if self.winner() is not None:                               #Check if the game is not over
            raise ValueError('Game is already over')
        self._board[i][j] = self._player                                  #Set the mark of the player at the position
        if self._player == 'X':                                     #Change the player for the next turn
            self._player = 'O'
        else:
            self._player = 'X'

    def _is_win(self, mark):
        '''Check whehter the board configuration is a win'''
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or  # row0
                mark == board[1][0] == board[1][1] == board[1][2] or  # row1
                mark == board[2][0] == board[2][1] == board[2][2] or  # row2
                mark == board[0][0] == board[1][0] == board[2][0] or  # column0
                mark == board[0][1] == board[1][1] == board[2][1] or  # column1
                mark == board[0][2] == board[1][2] == board[2][2] or  # column2
                mark == board[0][0] == board[1][1] == board[2][2] or  # diagonal1
                mark == board[0][2] == board[1][1] == board[2][0])    # diagonal2

    def winner(self):
        '''Return the mark that is Winner of the game'''
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        '''Return the string representation of the board'''
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)

game = TicTacToe()
game.mark(0,1)
game.mark(0,0)
game.mark(0,2)
game.mark(1,0)
game.mark(1,1)
game.mark(1,2)
game.mark(2,1)
print(game)
game.mark(2,2)
game.mark(2,0)
print(game)
game.winner()


