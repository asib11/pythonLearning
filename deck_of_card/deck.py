from random import shuffle
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        

    def __repr__(self) :
        return '{} of {}'.format(self.value, self.suit)


class Deck:
    def __init__(self):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self.cards = [Card(value, suit) for suit in suits for value in values]
    
    def count(self):
        return len(self.cards)

    def __repr__(self) :
        return 'Deck of {} cards'.format(self.count())

    def _deal(self, num):
        count = self.count()
        get_card = min([count,num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-get_card:]
        self.cards = self.cards[:-get_card]
        return cards

    def suffle(self):
        if self.count <52 :
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand):
        return self._deal(hand)


v1 = Deck()
print(v1.deal_card())
print(v1.deal_hand(5))
print(v1.count())