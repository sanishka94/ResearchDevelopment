import random

class Card:
	'''Represents a standard playing card'''
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = ['None', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

	def __init__(self, suit=0, rank=0):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

	def __lt_old__(self, other):
		# Check the suits
		if self.suit < other.suit: return True
		if self.suit > other.suit: return False

		# suits are the same, check the ranks
		return self.rank < other.rank

	def __lt__(self, other):
		t1 = self.suit, self.rank
		t2 = other.suit, other.rank
		return t1 < t2

class Deck:
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self, card):
		self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

	def sort(self):
		self.cards.sort()

	def deal_hands(self, nhands, nhcards):
		if nhands > 26:
			print('Too many players')
			return
		if nhands*nhcards > 52:
			print('Too many cards per player')
			return

		hands = []
		for i in range(1,nhands+1):
			hand = Hand('Player_%.d' % i)
			for j in range(nhcards):
				hand.add_card(self.pop_card())
			hands.append(hand)
			print(hand.label)
			print(hand, '\n')




class Hand(Deck):
	'''Represents a hand of playing cards'''
	def __init__(self, label=''):
		self.cards = []
		self.label = label

	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())

def find_defining_class(obj, meth_name):
	for ty in type(obj).mro():
		if meth_name in ty.__dict__:
			return ty

deck = Deck()
'''
queen_of_diamonds = Card(1, 12)
card1 = Card(2, 11)
print(card1)

print(deck)
deck.shuffle()
print(deck)
deck.sort()
print(deck)

hand  = Hand('new hand')
print(hand.cards)
print(hand.label)
card = deck.pop_card()
hand.add_card(card)
print(hand)
print(find_defining_class(hand, '__init__'))
'''
deck.shuffle()
deck.deal_hands(26, 2)