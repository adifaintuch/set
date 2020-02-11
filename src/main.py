# #set.py
# #Adi Faintuch
# #7/15/19

# '''
# -I will use pygame
# -I will have a model and a view

# for the model:
# 	-I will have a card namedtuple that has 4 attributes: color, shape,
# 	number, and shading
# 	-Each set will be a literal set object that contains 3 card
# 	namedtuple objects
# 	-I will have 2 lists: one for all of the cards in the "deck"
# 	and the other being a list of the made set objects

# 	-I will need an algorithm that checks to see if 3 cards make up a set
# 	according to the following rules:
# 	"Each card is unique in its four features: color (red, green
# 	or purple), shape (diamond, squiggle or oval), number (1, 2
# 	or 3 shapes), and shading (solid, striped or open). A set
# 	consists of three cards on which each individual feature is either
# 	all the same or all different on all three cards"
# 	-if you think that there are no sets left you can click "no sets
# 	possible" in which case an alogorithm will check if thats true and
# 	if so it will add 3 additional cards.

# 	-later I can also implement hints and algorithms to check if there
# 	are any sets left in the cards displayed on the screen

# for the view:
# 	-I can later make it also multi player but for now I'm only
# 	going to make it single player

# 	for single player:
# 		-I will have a screen with 12 cards objects displayed on it
# 		-when you click on a card it gets a yellow highlight around it
# 		-after you click on 3 cards you click the "set" button to make
# 		it into a set
# 		-if you click on a card again before clicking "set" it takes
# 		away the yellow highlight around that card
# 		-it does not let you click (highlight) more than 3 cards
# 		at the same time
# 		-everytime you make a set the cards dissapear, with 3 new cards
# 		replacing them, and your "set deck" now displays 1 more set (it
# 		shows the number of sets you currently have, beginning with zero)
# '''



#ok I need to make a dictionary, the key will be position (ex: 1, 2, etc..)
#and the value will be the card

import pygame
from random import shuffle
import model
from collections import defaultdict

clicked_image = pygame.image.load('/Users/adifaintuch/Desktop/set/src/clicked.png')



def get_card_num(card):
    card_num = 0
    if(card.color == 'green'):
        card_num += 27
    if(card.color == 'purple'):
        card_num += 54
    if(card.shape == 'oval'):
        card_num += 3
    if(card.shape == 'squiggle'):
        card_num += 6
    if(card.number == 2):
        card_num += 1
    if(card.number == 3):
        card_num += 2
    if(card.shading == 'striped'):
        card_num += 9
    if(card.shading == 'solid'):
        card_num += 18
    return card_num

def make_image_clicked(image_key, image_value, surface, image_list, displayed_cards):

    new_x = image_value.x - 5
    new_y = image_value.y - 5
    new_width = image_value.width + 10
    new_height = image_value.height + 10
    print("old x: ", image_value.x, " new x: ", new_x)
    print("old y: ", image_value.y, " new y: ", new_y)
    print("old width: ", image_value.width, " new width: ", new_width)
    print("old height: ", image_value.height, " new height: ", new_height)
    new_rect = pygame.Rect(new_x, new_y, new_width, new_height)

    pygame.draw.rect(surface, (255, 242, 56), new_rect)
    # surface.blit(pygame.image.load('/Users/adifaintuch/Desktop/set/src/clicked.png'), (new_x, new_y), new_rect)
    # print()
    # print("the image is ", image_key.position, image_list[image_key.position])
    # #surface.blit(pygame.image.load(image_list[image_key.position]),image_value)
    surface.blit(pygame.image.load('/Users/adifaintuch/Desktop/set/src/card' + str(image_key.position + 1) + '.png'), image_value)

def display_cards(displayed_cards, image_list, surface, displayed_images):
    pygame.display.set_mode((700, 600))

    upper_left_x = 40 #plus 230 each time
    upper_left_y = 30 #plus 149 every 3 cards

    current_card = 0
    for i in range(4):
        upper_left_x = 40
        for j in range(3):

<<<<<<< HEAD
            displayed_cards[current_card] = displayed_cards[current_card]._replace(x = upper_left_x)
            displayed_cards[current_card] = displayed_cards[current_card]._replace(y = upper_left_y)
=======
            # right HERE
            displayed_cards[current_card] = displayed_cards[current_card]._replace(x = upper_left_x)
            displayed_cards[current_card] = displayed_cards[current_card]._replace(y = upper_left_y)
            # displayed_cards[current_card] = displayed_cards[current_card]._replace(width = image_list[displayed_cards[current_card].position.get_width())
            # displayed_cards[current_card] = displayed_cards[current_card]._replace(height = image_list[displayed_cards[current_card].position.get_height())
>>>>>>> 15c3f937b41cd6eec21301a98617babf2fd2f621

            print('testing here ', image_list[displayed_cards[current_card].position])
            current_rect = surface.blit(image_list[displayed_cards[current_card].position], (upper_left_x, upper_left_y))
            displayed_images[displayed_cards[current_card]] = current_rect

<<<<<<< HEAD


            upper_left_x += 230
            current_card += 1
        upper_left_y += 149


def find_index_of_card(card, displayed_cards):
    '''finds the index of the clicked card in the displayed_cards list'''
    for i in range(len(displayed_cards)):
        if(card == displayed_cards[i]):
            return i;

=======
            # displayed_cards[current_card] = displayed_cards[current_card]._replace(width = current_rect.width)
            # displayed_cards[current_card] = displayed_cards[current_card]._replace(height = current_rect.height)

            # dict_of_displayed_cards[current_rect] = displayed_cards[current_card]




            upper_left_x += 230
            current_card += 1
        upper_left_y += 149
>>>>>>> 15c3f937b41cd6eec21301a98617babf2fd2f621

def run():
    total_score = 0;

    pygame.init()

<<<<<<< HEAD
=======
    # clicked_image = pygame.image.load('/Users/adifaintuch/Desktop/set/src/clicked.png')
    #
    # rect_1 = pygame.Rect(0, 0, 230, 149)
    # rect_2 = pygame.Rect(250, 20, 230, 149)
    # rect_3 = pygame.Rect(480, 20, 230, 149)
    # rect_4 = pygame.Rect(20, 169, 230, 149)
    # rect_5 = pygame.Rect(250, 169, 230, 149)
    # rect_6 = pygame.Rect(480, 169, 230, 149)
    # rect_7 = pygame.Rect(20, 318, 230, 149)
    # rect_8 = pygame.Rect(250, 318, 230, 149)
    # rect_9 = pygame.Rect(480, 318, 230, 149)
    # rect_10 = pygame.Rect(20, 467, 230, 149)
    # rect_11 = pygame.Rect(250, 467, 230, 149)
    # rect_12 = pygame.Rect(480, 467, 230, 149)


>>>>>>> 15c3f937b41cd6eec21301a98617babf2fd2f621
    list_of_rect = []

    #first item is the card number (0-11),
    #the second if a dict of card, rect, and surface
    dict_of_displayed_cards = defaultdict()

    for i in range(11):
        rect_to_add = 'rect' + str(i + 1)
        list_of_rect.append(rect_to_add)


    surface = pygame.display.set_mode((700, 600))

    running = True

    deck = model.create_deck()
    shuffle(deck)

<<<<<<< HEAD
    #displayed_cards is a list of card objects
=======
>>>>>>> 15c3f937b41cd6eec21301a98617babf2fd2f621
    displayed_cards = model.create_initial_twelve_cards(deck)
    model.remove_used_cards_from_deck(deck, displayed_cards)

    image_list = []

    for i in range(81):
        new_pathname = '/Users/adifaintuch/Desktop/set/src/card' + str(i + 1) + '.png'
        image_list.append(pygame.image.load(new_pathname))

    #a defaultdict of key = card and value = rect
    displayed_images = defaultdict()

    #a defaultdict of key = card and value = rect
    clicked_images = defaultdict()

    display_cards(displayed_cards, image_list, surface, displayed_images)

    for i in displayed_images:
        print("displayed images", i)

#currently, the problem is that the old cards are still on the screen
#I should just reinstantiate the entire screen

<<<<<<< HEAD
    clicks = 0

    set_of_removed_cards = set()

    while running:
        for event in pygame.event.get():
            if(clicks < 3):
=======

    while running:
        for event in pygame.event.get():
            if(len(clicked_images) < 3):
                print("len is less than 3\n")
>>>>>>> 15c3f937b41cd6eec21301a98617babf2fd2f621
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
<<<<<<< HEAD
                    clicks += 1
                    for key, value in displayed_images.items():
                        if value.collidepoint(pos):
                            if(key not in set_of_removed_cards):
                                clicked_images[key] = value
                                make_image_clicked(key, value, surface, image_list, displayed_cards)
            else:
                clicks = 0
=======
                    for key, value in displayed_images.items():
                        if value.collidepoint(pos):
                            clicked_images[key] = value
                            make_image_clicked(key, value, surface, image_list, displayed_cards)
            else:
                print("len is more than 3\n")
>>>>>>> 15c3f937b41cd6eec21301a98617babf2fd2f621
                for item in clicked_images:
                    print("item is: ", item, "/n")
                is_a_set = model.check_for_set(clicked_images)
                if(is_a_set):
                    #print out "You got a set!" on the screen
                    #remove those cards from the screen and from the deck
                    #place new cards in their place
                    #increase score by 1
                    print("is a set")
                    total_score += 1;
                    for fgh in displayed_cards:
                        print("displayed cards ", fgh, "\n")
<<<<<<< HEAD
                    list_of_index = []
                    for card in clicked_images:
                        print("card is ", card, "\n")
                        print("position is ", find_index_of_card(card, displayed_cards), "\n")
                        list_of_index.append(find_index_of_card(card, displayed_cards))
                        set_of_removed_cards.add(card)
                        #displayed_cards.remove(card)
                        #displayed_images.pop(card)


                    clicked_images = defaultdict()
                    model.add_three_new_cards(deck, displayed_cards, list_of_index)
=======
                    for card in clicked_images:
                        print("card is ", card, "\n")
                        displayed_cards.remove(card)
                        displayed_images.pop(card)

                    clicked_images = defaultdict()
                    model.add_three_new_cards(deck, displayed_cards, displayed_images)
                    #print("2total num of cards is ", len(displayed_cards))
>>>>>>> 15c3f937b41cd6eec21301a98617babf2fd2f621
                    display_cards(displayed_cards, image_list, surface, displayed_images)
                else:
                    clicked_images = defaultdict()
                    print("len of clicked images ", len(clicked_images))
                    display_cards(displayed_cards, image_list, surface, displayed_images)
                    #print out "Not a set" on the screen
                    #remove just the yellow highlights around the cards
                    print("is not a set")



        pygame.display.flip()


    pygame.quit()


if __name__ == '__main__':
	run()
