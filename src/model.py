#model.py
from random import shuffle
from collections import namedtuple

Card = namedtuple('Card', 'color, shape, number, shading, position, x, y')

#Card = namedtuple('Card', 'color, shape, number, shading, x, y')

def create_deck():
	'''creates the deck of cards and returns a list of card namedtuples'''
	colors = ['red', 'green', 'purple']
	shapes = ['diamond', 'squiggle', 'oval']
	number = [1, 2, 3]
	shading = ['solid', 'striped', 'open']

	deck = []

	card_pos = 0
	for c in colors:
		for s in shapes:
			for n in number:
				for sh in shading:
					new_card = Card(c, s, n, sh, card_pos, 0, 0)
					#new_card = Card(c, s, n, sh, 0, 0)
					deck.append(new_card)
					card_pos += 1

	return deck

def create_initial_twelve_cards(deck):
	'''returns a list of 12 card objects'''
	used_cards = []
	for i in range(12):
		used_cards.append(deck[i])
	return used_cards

def add_three_new_cards(deck, displayed_cards):
	'''adds 3 new cards to the displayed_cards list'''
	for i in range(3):
		displayed_cards.append(deck[i])

def remove_used_cards_from_deck(deck, used_cards):
	'''removed the used cards from the deck'''
	for card in used_cards:
		deck.remove(card)

def check_for_set(card_dict):
	'''checks to see if a dictionary of 3 cards is a set'''
 	# all_diff_numbers = False;
 	# all_diff_colors = False;
 	# all_diff_shapes = False;
 	# all_diff_shading = False;

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
	# if(len(colors_set) == 3):
	# 	all_diff_colors = True
	# if(len(shapes_set) == 3):
	# 	all_diff_shapes = True
	# if(len(shading_set) == 3):
	# 	all_diff_shading = True
	# return((all_diff_colors && all_diff_shapes && all_diff_shading) || (!all_diff_colors && !all_diff_shades && !all_diff_shading))
