'''
set.py
Adi Faintuch
7/15/19
'''
'''
Some thing that I need to do:
-make sure the game doesn't crash when you run out of cards in the sets
    -simply continue without adding cards
        -can cover the cards with a black spot

-make a button that the user can click if they think there is no set
    -if there is a set, let them know
    -otherwise, add 3 new cards to the board
-make a hint button in which the user can click and it will highlight one card
that is part of the set
    -will do it for each hint
    -if they click on the highlighted card, it becomes a regularly clicked card

-fill in the README
    -good link: https://thehftguy.com/2016/10/24/heres-how-to-make-a-good-github-project-for-your-resume/
'''

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
    new_rect = pygame.Rect(new_x, new_y, new_width, new_height)

    pygame.draw.rect(surface, (255, 242, 56), new_rect)
    surface.blit(pygame.image.load('/Users/adifaintuch/Desktop/set/src/card' + str(image_key.position + 1) + '.png'), image_value)

def make_image_unclicked(image_key, image_value, surface, image_list, displayed_cards):
    new_x = image_value.x - 5
    new_y = image_value.y - 5
    new_width = image_value.width + 10
    new_height = image_value.height + 10
    new_rect = pygame.Rect(new_x, new_y, new_width, new_height)

    pygame.draw.rect(surface, (0, 0, 0), new_rect)
    surface.blit(pygame.image.load('/Users/adifaintuch/Desktop/set/src/card' + str(image_key.position + 1) + '.png'), image_value)

def display_cards(displayed_cards, image_list, surface, displayed_images, total_score):
    pygame.display.set_mode((700, 600))

    upper_left_x = 40 #plus 230 each time
    upper_left_y = 30 #plus 149 every 3 cards

    current_card = 0
    for i in range(4):
        upper_left_x = 40
        for j in range(3):
            current_rect = surface.blit(image_list[displayed_cards[current_card].position], (upper_left_x, upper_left_y))
            displayed_images[displayed_cards[current_card]] = current_rect
            print()
            print("CURRENT CARD")
            print(current_card)
            print("IN DISPLAYED IMAGES")
            print(displayed_cards[current_card])
            print("CURRENT RECT")
            print(current_rect)
            print()

            upper_left_x += 230
            current_card += 1
        upper_left_y += 149

    display_score(surface, total_score)


def find_index_of_card(card, displayed_cards):
    '''finds the index of the clicked card in the displayed_cards list'''
    for i in range(len(displayed_cards)):
        if(card == displayed_cards[i]):
            return i;

def print_set(displayed_cards):
    '''prints a set solution'''
    set = model.find_a_set(displayed_cards)
    if(set == []):
        print("set is empty")
    else:
        for card in set:
            print("card in set: ", card, "\n")

def display_score(surface, total_score):
    font = pygame.font.Font(None, 30)
    to_print = "score: " + str(total_score)
    text = font.render(to_print, True, [0, 0, 255])
    text_rect = text.get_rect(center =(345, 580))
    surface.blit(text, text_rect)

def display_end_score(surface, total_score):
    '''displays the score at the end of the game'''
    font = pygame.font.Font(None, 100)
    to_print = "TOTAL SCORE: " + str(total_score)
    text = font.render(to_print, True, [0, 0, 250])
    text_rect = text.get_rect(center =(350, 500))
    surface.blit(text, text_rect)

def display_end_game(surface, total_score):
    '''handles the end of the game display'''
    pygame.display.set_mode((700, 600))
    game_over_rect = pygame.Rect(-75,0,350,350)
    surface.blit(pygame.image.load('/Users/adifaintuch/Desktop/set/src/gameover.jpg'), game_over_rect)
    display_end_score(surface,total_score)

def run():
    total_score = 0;

    pygame.init()

    list_of_rect = []


    #first item is the card number (0-11),
    #the second if a dict of card, rect, and surface
    dict_of_displayed_cards = defaultdict()

    for i in range(11):
        rect_to_add = 'rect' + str(i + 1)
        list_of_rect.append(rect_to_add)


    surface = pygame.display.set_mode((700, 600))



    running = True
    waiting_for_end = False

    deck = model.create_deck()
    print("DECK")
    for i in range(len(deck)):
        print(deck[i])
        print()
    print()
    shuffle(deck)

    #displayed_cards is a list of card objects
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

    display_cards(displayed_cards, image_list, surface, displayed_images, total_score)

    clicks = 0
    set_of_removed_cards = set()

    solution_set = []

    print_solution_set_once = False
    while running:
        for event in pygame.event.get():
            if(len(deck) == 0 and len(solution_set) == 0):
                display_end_game(surface, total_score)
                running = False
                waiting_for_end = True
            #print_set(displayed_cards)
            if(clicks < 3):
                solution_set = model.find_a_set(displayed_cards)
                if(print_solution_set_once == False):
                    print_solution_set_once = True
                    print("displayed_images")
                    print(displayed_images)
                    print("displayed cards")
                    print(displayed_cards)
                    print("solution set")
                    print(solution_set)
                    print("size of deck", len(deck))
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for key, value in displayed_images.items():
                        if value.collidepoint(pos):
                            if(key not in set_of_removed_cards):
                                if(key not in clicked_images):
                                    clicks += 1
                                    clicked_images[key] = value
                                    make_image_clicked(key, value, surface, image_list, displayed_cards)
                                else:
                                    clicks -= 1
                                    make_image_unclicked(key, value, surface, image_list, displayed_cards)
                                    del clicked_images[key]
            else:
                clicks = 0
                is_a_set = model.check_for_set(clicked_images)
                if(is_a_set):
                    print_solution_set_once = False
                    print("is a set")
                    total_score += 1;
                    list_of_index = []
                    for card in clicked_images:
                        list_of_index.append(find_index_of_card(card, displayed_cards))
                        set_of_removed_cards.add(card)
                    print("removed cards")
                    print(set_of_removed_cards)
                    clicked_images = defaultdict()
                    if(len(deck) != 0):
                        model.add_three_new_cards(deck, displayed_cards, list_of_index)
                    #else:
                        #model.remove_three_cards(deck, displayed_cards, list_of_index)
                    display_cards(displayed_cards, image_list, surface, displayed_images, total_score)
                else:
                    print("is not a set")
                    clicked_images = defaultdict()
                    display_cards(displayed_cards, image_list, surface, displayed_images, total_score)



        pygame.display.flip()

        while waiting_for_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    pygame.quit()


if __name__ == '__main__':
	run()
