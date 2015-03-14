"""Module for defining deck data"""
class Card:
    """class for defining card"""
    suit = 0
    rank = 0
    VALUES = {
            1: 'Ace',
            11: 'Jack',
            12: 'Queen',
            13: 'King',
            }
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def get_rank(self):
        return self.rank
    def get_card_name(self):
        if self.get_rank in self.VALUES:
            return self.VALUES[self.rank]
        else:
            return '' + self.get_rank

class Deck:
    """Object for representing deck of 52 cards"""
    deckList = []
    def __init__(self):
        for i in range(0, 4):
            for j in range(0, 52):
               self.deckList[j] = Card(i, j)
