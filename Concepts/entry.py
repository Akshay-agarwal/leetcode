class Entry(object):
    '''Entry of a score of a game'''
    def __init__(self, name, score):
        '''initializes the entry with given score and name of the player'''
        self._score = score
        self._name = name

    def get_name(self):
        '''Return name of the player for the entry'''
        return self._name

    def get_score(self):
        '''Return score of the entry'''
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)
