from deck import Deck
def hit(deck):
    return deck.pull_from_deck()
def deal(deck):
    """Deal the next card"""
    deck.shuffle()
    return hit(deck)

def main():
    print "Game initialized"
    game()

def calculate_hand_val(hand):
    value = 0
    for card in hand:
        num_aces = 0
        if card.get_card_name() == 'Ace':
            num_aces += 1
        else:
            value = value + card.get_rank()
        if value + num_aces * 11 > 21:
            value += num_aces
        else:
            value += num_aces * 11
    return value
def show_all_cards_in_hand(hand):
    for card in hand:
        print card.get_card_name() + ", ",

def game():
    deck = Deck()
    player_hand = []
    player_hand.append(deal(deck))
    show_all_cards_in_hand(player_hand)

    decision = None

    while decision != 3:
        print #For new line
        decision = input('Press 1 to hit, 2 to stand, 3 to exit: ')
        if(decision == 1):
            player_hand.append(hit(deck))
            show_all_cards_in_hand(player_hand)
if __name__ == "__main__":
    main()


