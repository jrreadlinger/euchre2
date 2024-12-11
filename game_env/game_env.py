import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self, trump, lead):
        '''
        
        Value (high to low):
            Jack of Trump Suit (Right Bower)
            Jack of Same Color Suit (Left Bower)
            Highest Trump Card (excluding Bowers)
            High Lead Card (excluding Bowers)
        '''


    def __repr__(self):
        return f"Card({self.suit=}, {self.rank=})"
    
    def __str__(self):
        rank_dict = {'9': 'Nine', '10': 'Ten', 'J': 'Jack',
                     'Q': 'Queen', 'K': 'King', 'A': 'Ace'}
        suit_dict = {'C': 'Clubs', 'D': 'Diamonds',
                     'H': 'Hearts', 'S': 'Spades'}
        rank_str = rank_dict[self.rank]
        suit_str = suit_dict[self.suit]
        return rank_str + " of " + suit_str


class Deck:
    def __init__(self):
        suits = ['C','D','H','S']
        ranks = ['9','10','J','Q','K','A']
        self.cards = [Card(suit,rank) for suit in suits for rank in ranks]

    def deal(self, n):
        '''
        Deal n cards
        '''
        dealt_cards = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt_cards

    def shuffle(self):
        '''
        Shuffle the cards
        '''
        random.shuffle(self.cards)

    def __repr__(self):
        return f"Deck({self.cards=})"


class Trick:
    def __init__(self, trump):
        self.trump = trump
        self.lead = None
        self.cards_played = []

    def play_card(self, card):
        '''
        Play card to the trick
        '''
        if not self.cards_played:
            self.lead = card.suit 
        self.cards_played.append(card)

    def determine_winner(self):
        '''
        Determine the trick winner
        '''
        card1 = self.cards_played[0]
        card2 = self.cards_played[1]

class Game:
    def __init__(self):
        pass

    def updateScore(self):
        '''
        Update the game score
        '''
        pass

    def selectTrump(self):
        '''
        Select the trump suit
        '''
        pass

def main():
    deck = Deck()
    print(len(deck))
    for card in deck.cards:
        print(card)

if __name__ == "__main__":
    main()