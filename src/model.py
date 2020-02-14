#model.py
from random import shuffle
from collections import namedtuple
from itertools import combinations

Card = namedtuple('Card', 'color, shape, number, shading, position')

#Card = namedtuple('Card', 'color, shape, number, shading, x, y')

def create_deck():
	'''creates the deck of cards and returns a list of card namedtuples'''
	colors = ['red', 'green', 'purple']
	shapes = ['diamond', 'oval', 'squiggle']
	number = [1, 2, 3]
	shading = ['open', 'striped', 'solid']

	deck = []

	card_pos = 0
	for c in colors:
		for sh in shading:
			for s in shapes:
				for n in number:
					new_card = Card(c, s, n, sh, card_pos)
					deck.append(new_card)
					card_pos += 1

	return deck

def create_initial_twelve_cards(deck):
	'''returns a list of 12 card objects'''
	used_cards = []
	for i in range(12):
		used_cards.append(deck[i])
	return used_cards

def add_three_new_cards(deck, displayed_cards, list_of_index):
	'''adds 3 new cards to the displayed_cards list'''
	for i in range(3):
		print("testing0 ", i, "\n")
		print("testing1 ", list_of_index[i], "\n")
		print("testing2 ", deck[i], "\n")
		displayed_cards[list_of_index[i]] = deck[i]

def add_three_new_cards(deck, displayed_cards, list_of_index):
	'''adds 3 new cards to the displayed_cards list and removes them from deck'''
	for i in range(3):
		displayed_cards[list_of_index[i]] = deck[i]
	for j in range(3):
		deck.remove(displayed_cards[list_of_index[j]])
	# for j in range(3):
	# 	deck.remove(displayed_cards[list_of_index[i]])

def remove_used_cards_from_deck(deck, used_cards):
	'''removed the used cards from the deck'''
	for card in used_cards:
		deck.remove(card)


def check_for_set(card_dict):
	'''checks to see if a dictionary of 3 cards is a set'''

	numbers_set = set()
	colors_set = set()
	shapes_set = set()
	shading_set = set()

	for k in card_dict.keys():
		numbers_set.add(k.number)
		colors_set.add(k.color)
		shapes_set.add(k.shape)
		shading_set.add(k.shading)
	if(len(numbers_set) == 2 or len(colors_set) == 2 or len(shapes_set) == 2 or len(shading_set) == 2):
		 return False
	return True

def check_for_set_list(card_list):
	'''checks to see if a list of 3 cards is a set'''
	numbers_set = set()
	colors_set = set()
	shapes_set = set()
	shading_set = set()

	for k in card_list:
		numbers_set.add(k.number)
		colors_set.add(k.color)
		shapes_set.add(k.shape)
		shading_set.add(k.shading)
	if(len(numbers_set) == 2 or len(colors_set) == 2 or len(shapes_set) == 2 or len(shading_set) == 2):
		 return False
	return True

def find_a_set(displayed_cards):
	'''returns a list with 3 cards that make a set (the first one found -
	returns an empty list if no set is found'''

	list_of_combinations = list(combinations(displayed_cards, 3))
	for combo in list_of_combinations:
		if(check_for_set_list(combo)):
			return list(combo)
	return []
