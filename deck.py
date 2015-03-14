"""Module for defining deck data"""
class Deck:
    """Object for representing deck of 52 cards"""
    def __init__(self):
        for i in range(0, 52):
            self.list = i
