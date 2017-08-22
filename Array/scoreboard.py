from entry import Entry
import sys

class Scoreboard(object):
    '''A scoreboard for a game'''

    def __init__(self, capacity = 10):
        ''' Initialize the board with max capcity'''
        self._board = [None] * capacity     #create a new scoreboard with given capacity
        self._n = 0                         #initialize the number of elements in the scoreboard to 0

    def __getitem__(self, k):
        '''Used to get the value of an item at index k'''
        if (self._board[k] is not None):                 #check if value is present at the index
            return self._board[k]
        return ValueError('No value at the given Index')

    def __str__(self):
        """Return a string representation of the board"""
        return '/n'.join(str(self._board[j]) for j in range(self._n))

    def add_score(self, entry):
        '''Check if the new score can be added to the high scores'''
        score = entry.get_score()

        #A score is good score if the length of the board is less then the number of scores added
        #or if the new score is greater then the last score in the board
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            #shift the lower score rightwards to make room for new score
            j = self._n - 1
            while j > 0 and self._board[j].get_score < score:
                self._board[j] = self._board[j]
                j -= 1
            self._board[j] = entry







