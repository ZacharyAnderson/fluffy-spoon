import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return repr("{} of {}".format(self.value, self.suit))

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw_card(self):
        return self.cards.pop()

    def return_card(self, card):
        self.cards.append(card)


class Player:
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


if __name__ == "__main__":
    deck = Deck()

    print(deck.cards)
    deck.show()
