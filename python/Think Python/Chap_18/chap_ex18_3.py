import random
hist = {}

class Card:
    """Represents a standard playing card.
    
    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __eq__(self, other):
        """Checks whether self and other have the same rank and suit.

        returns: boolean
        """
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        """Compares this card to other, first by suit, then rank.

        returns: boolean
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """
    
    def __init__(self):
        """Initializes the Deck with 52 cards.
        """
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Returns a string representation of the deck.
        """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck.

        card: Card
        """
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there.
        
        card: Card
        """
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):
    """Represents a hand of playing cards."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label

class PokerHand(Hand):
    """Represents a poker hand."""
    classes = ['pair', 'two pair', 'three of a kind', 'straight', 'flush', 'full house', 'four of a kind', 'straight flush']

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_two_pair(self):
        self.rank_hist()
        match = 0
        for val in self.ranks.values():
            if val >= 2:
                match += 1
        if match >= 2:
            return True
        return False

    def has_three_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_four_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def in_order(self, alist):
        pre = alist[0]
        match = 0
        for val in alist:
            x, y = divmod(pre+1, 14)
            if y == val:
                match += 1
            elif pre == val:
                match = match
            else:
                match = 0
            pre = val
        if match == 4:
            return True
        return False

    def has_straight(self):
        self.rank_hist()
        li = []
        for val in self.ranks:
            li.append(val)
        li.sort()
        return self.in_order(li)

    def has_full_house(self):
        self.rank_hist()
        cond = False
        for val in self.ranks:
            if self.ranks[val] >= 3:
                has = val
                cond = True
        if cond:
            self.ranks.pop(has)
            for val in self.ranks.values():
                if val >= 2:
                    return True
        return False

    def has_straight_flush(self):
        self.suit_hist()
        ssuit = None
        for val in self.suits:
            if self.suits[val] >=5:
                ssuit = val
        if ssuit == None: return False

        clist = []
        for item in self.cards:
            s, r = item.suit, item.rank
            if s == ssuit: clist.append(r)
        clist.sort()
        return self.in_order(clist)

    def classify(self):
        self.label = "none"
        if self.has_pair(): self.label = self.classes[0]
        if self.has_two_pair(): self.label = self.classes[1]
        if self.has_three_of_a_kind(): self.label = self.classes[2]
        if self.has_straight(): self.label = self.classes[3]
        if self.has_flush(): self.label = self.classes[4]
        if self.has_full_house(): self.label = self.classes[5]
        if self.has_four_of_a_kind(): self.label = self.classes[6]
        if self.has_straight_flush(): self.label = self.classes[7]

def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None

def play_poker(players):
    global hist
    deck = Deck()
    deck.shuffle()
    if 2 > players or players > 7:
        print('Too many players, cannot play')
        return

    for i in range(players):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        hand.classify()
        hist[hand.label] = hist.get(hand.label, 0) + 1

def prob_table(di, tot):
    print('Probability', 'Classification', sep='\t\t')

    for val in hist:
        prob = (tot / hist[val])
        print('One time in %.2f' % prob, '\t\t', val)
    

x, y = 100000, 7
for i in range(x):
    step, ot = divmod(x, 20)
    istep, ot = divmod(i, step)
    if ot == 0: print(i)
    play_poker(y)

prob_table(hist, x*y)