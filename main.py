from deck import Deck
def deal():
    """Deal the next card"""
    deck = Deck()
    deck.shuffle()
    print deck.pull_from_deck().get_card_name()

def main():
    print "Game initialized"
    deal()
if __name__ == "__main__":
    main()


