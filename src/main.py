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
    surface.blit(image_key.image, image_value)

def make_image_unclicked(image_key, image_value, surface, image_list, displayed_cards):
    new_x = image_value.x - 5
    new_y = image_value.y - 5
    new_width = image_value.width + 10
    new_height = image_value.height + 10
    new_rect = pygame.Rect(new_x, new_y, new_width, new_height)

    pygame.draw.rect(surface, (0, 0, 0), new_rect)
    surface.blit(image_key.image, image_value)

def make_player_clicked(x, y, width, height, surface, player1_clicked, player2_clicked):
    '''makes the player1 or player2 card clicked'''
    new_x = x - 5
    new_y = y - 5
    new_width = width + 10
    new_height = height + 10
    new_rect = pygame.Rect(new_x, new_y, new_width, new_height)

    pygame.draw.rect(surface, (255, 242, 56), new_rect)

    if(player1_clicked):
        display_player1(surface)
    else:
        display_player2(surface)

def make_player_unclicked(x, y, width, height, surface, player1_clicked, player2_clicked):
    '''makes the player1 or player2 card unclicked'''
    new_x = x - 5
    new_y = y - 5
    new_width = width + 10
    new_height = height + 10
    new_rect = pygame.Rect(new_x, new_y, new_width, new_height)

    pygame.draw.rect(surface, (0, 0, 0), new_rect)

    if(player1_clicked):
        display_player1(surface)
    else:
        display_player2(surface)

def create_initial_display_card_positions(displayed_cards):
    '''created the initial displayed_cards positions'''
    upper_left_x = 40 #plus 230 each time
    upper_left_y = 30 #plus 149 every 3 cards

def display_cards_initial(displayed_cards, image_list, surface, total_score, deck_size, single_player, player1_score, player2_score):
    #pygame.display.set_mode((700, 600))
    if(single_player):
        pygame.display.set_mode((700, 750))
        display_score_single(surface, total_score)
    else:
        pygame.display.set_mode((1000, 750))
        display_players(surface)
        display_score_multi(surface, player1_score, player2_score)

    upper_left_x = 40 #plus 230 each time
    upper_left_y = 30 #plus 149 every 3 cards

    current_card = 0

    cards_to_display_list = list(displayed_cards.keys())
    for i in range(4):
        upper_left_x = 40
        for j in range(3):
            #card_image = pygame.transform.scale(cards_to_display_list[current_card].image, (158, 88))
            #current_rect = surface.blit(card_image, (upper_left_x, upper_left_y))
            current_rect = surface.blit(cards_to_display_list[current_card].image, (upper_left_x, upper_left_y))
            displayed_cards[cards_to_display_list[current_card]] = current_rect

            upper_left_x += 230
            current_card += 1
        upper_left_y += 149

    display_deck_size(surface, deck_size)
    display_no_set_button(surface)
    display_get_hint_button(surface)
    return displayed_cards

def display_cards_later(displayed_cards, image_list, surface, total_score, deck_size, single_player, player1_score, player2_score):
    #pygame.display.set_mode((700, 600))
    if(single_player):
        pygame.display.set_mode((700, 750))
        display_score_single(surface, total_score)
    else:
        pygame.display.set_mode((1000, 750))
        display_players(surface)
        display_score_multi(surface, player1_score, player2_score)

    for k,v in displayed_cards.items():
        current_rect = surface.blit(k.image, v)

    display_deck_size(surface, deck_size)
    display_no_set_button(surface)
    display_get_hint_button(surface)
    return displayed_cards

def get_rect_of_card(card, displayed_cards):
    '''returns the rect of the clicked card in the displayed_cards list'''
    rect = displayed_cards[card]
    return rect

def print_set(displayed_cards):
    '''prints a set solution'''
    set = model.find_a_set(displayed_cards)
    if(set == []):
        print("set is empty")
    else:
        for card in set:
            print("card in set: ", card, "\n")

def display_score_single(surface, total_score):
    '''displays the score for singleplayer'''
    font = pygame.font.Font(None, 50)
    #print("FONTS ARE: ", pygame.font.get_fonts())

    to_print = "score: " + str(total_score)
    text = font.render(to_print, True, [255, 255, 255])
    text_rect = text.get_rect(center =(350, 650))
    surface.blit(text, text_rect)

def display_score_multi(surface, player1_score, player2_score):
    '''displays the score for multiplayer'''
    font = pygame.font.Font(None, 50)
    #print("FONTS ARE: ", pygame.font.get_fonts())

    to_print1 = "player 1 score: " + str(player1_score)
    text = font.render(to_print1, True, [255, 255, 255])
    text_rect = text.get_rect(center =(840, 345))
    surface.blit(text, text_rect)

    to_print2 = "player 2 score: " + str(player2_score)
    text = font.render(to_print2, True, [255, 255, 255])
    text_rect = text.get_rect(center =(840, 545))
    surface.blit(text, text_rect)

def display_deck_size(surface, deck_size):
    '''displays the size of the deck'''
    font = pygame.font.Font(None, 50)
    to_print = "cards left in deck: " + str(deck_size)
    text = font.render(to_print, True, [255, 255, 255])
    text_rect = text.get_rect(center = (350, 723))
    surface.blit(text, text_rect)

def display_end_score(surface, total_score):
    '''displays the score at the end of the game'''
    font = pygame.font.Font(None, 100)
    to_print = "score: " + str(total_score)
    text = font.render(to_print, True, [0, 0, 250])
    text_rect = text.get_rect(center =(350, 500))
    surface.blit(text, text_rect)

def display_end_game(surface, total_score):
    '''handles the end of the game display'''
    #pygame.display.set_mode((700, 600))
    pygame.display.set_mode((700, 750))
    game_over_rect = pygame.Rect(-75,0,350,350)
    surface.blit(pygame.image.load('/Users/adifaintuch/Desktop/set/src/gameover.jpg'), game_over_rect)
    display_end_score(surface,total_score)

def display_no_set_button(surface):
    no_set_rect = pygame.Rect(30,600,5,5)
    no_set_image = pygame.image.load('/Users/adifaintuch/Desktop/set/src/noset.png')
    #no_set_image = pygame.transform.scale(no_set_image, (240, 58))
    surface.blit(no_set_image, no_set_rect)

def display_get_hint_button(surface):
    get_hint_rect = pygame.Rect(430,600,5,5)
    get_hint_image = pygame.image.load('/Users/adifaintuch/Desktop/set/src/gethint.png')
    #get_hint_image = pygame.transform.scale(get_hint_image, (240, 50))
    surface.blit(get_hint_image, get_hint_rect)

def create_displayed_cards(initial_cards):
    '''creates the initial 12 cards for display_cards'''
    displayed_cards_return = defaultdict()
    for card in initial_cards:
        displayed_cards_return[card] = pygame.Rect(0,0,0,0)
    return displayed_cards_return

def reset_board(surface, deck, displayed_cards, image_list, total_score, player1_score, player2_score):
    model.add_cards_back_to_deck(deck, displayed_cards)
    shuffle(deck)
    initial_cards = model.create_initial_twelve_cards(deck)
    displayed_cards = create_displayed_cards(initial_cards)
    model.remove_used_cards_from_deck(deck, displayed_cards.keys())
    clicked_images = defaultdict()
    displayed_cards_return = display_cards_initial(displayed_cards, image_list, surface, total_score, len(deck), single_player, player1_score, player2_score)
    return displayed_cards_return

def click_card_in_set(surface, image_list, displayed_cards, solution_set, clicked_images):
    '''clicks on a card in the solution set when user clicks on 'get hint' button'''
    for k,v in displayed_cards.items():
        if (k in solution_set and k not in clicked_images):
            clicked_images[k] = v
            make_image_clicked(k, v, surface, image_list, displayed_cards)
            break

def make_player_selection_screen(surface):
    '''makes the initial screen where the user can select single or multi player'''
    pygame.display.set_mode((700, 750))
    single_player_rect = pygame.Rect(150,200,5,5)
    single_player_image = pygame.image.load('/Users/adifaintuch/Desktop/set/src/singleplayer.png')
    #no_set_image = pygame.transform.scale(no_set_image, (240, 58))
    surface.blit(single_player_image, single_player_rect)

    multi_player_rect = pygame.Rect(150,400,5,5)
    multi_player_image = pygame.image.load('/Users/adifaintuch/Desktop/set/src/multiplayer.png')
    #get_hint_image = pygame.transform.scale(get_hint_image, (240, 50))
    surface.blit(multi_player_image, multi_player_rect)

def display_player1(surface):
    '''displays player 1'''
    player1_rect = pygame.Rect(675,200,316,98)
    player1_image = pygame.image.load('/Users/adifaintuch/Desktop/set/src/player1.png')
    surface.blit(player1_image, player1_rect)

def display_player2(surface):
    '''displays player 2'''
    player2_rect = pygame.Rect(675,400,316,98)
    player2_image = pygame.image.load('/Users/adifaintuch/Desktop/set/src/player2.png')
    surface.blit(player2_image, player2_rect)

def display_players(surface):
    '''displays players 1 and 2 and their scores'''
    display_player1(surface)
    display_player2(surface)


def run():
    total_score = 0
    player1_score = 0
    player2_score = 0

    pygame.init()

    list_of_rect = []

    for i in range(11):
        rect_to_add = 'rect' + str(i + 1)
        list_of_rect.append(rect_to_add)


    #surface = pygame.display.set_mode((700, 600))
    initial_surface = pygame.display.set_mode((700, 750))

    make_player_selection_screen(initial_surface)

    single_player = False

    _waiting = True
    while(_waiting):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _waiting = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                single_player_rect = pygame.Rect(150,200,402,98)
                multi_player_rect = pygame.Rect(150,400,402,98)
                if(single_player_rect.collidepoint(pos)):
                    single_player = True
                    print("!!SINGLE PLAYER? ", single_player)
                    _waiting = False
                elif(multi_player_rect.collidepoint(pos)):
                    _waiting = False
        pygame.display.flip()


    surface = pygame.display.set_mode((700, 750))

    print("SINGLE PLAYER? ", single_player)
    if(single_player == False):
        surface = pygame.display.set_mode((1000, 750))


    running = True
    find_solution_set = True

    deck = model.create_deck()
    shuffle(deck)

    initial_cards = model.create_initial_twelve_cards(deck)
    displayed_cards = create_displayed_cards(initial_cards)
    model.remove_used_cards_from_deck(deck, displayed_cards.keys())

    image_list = []

    for i in range(81):
        new_pathname = '/Users/adifaintuch/Desktop/set/src/card' + str(i + 1) + '.png'
        image_list.append(pygame.image.load(new_pathname))

    #a defaultdict of key = card and value = rect
    clicked_images = defaultdict()

    display_cards_initial(displayed_cards, image_list, surface, total_score, len(deck), single_player, player1_score, player2_score)

    clicks = 0
    set_of_removed_cards = set()

    solution_set = []

    print_solution_set_once = False

    player1_clicked = False
    player2_clicked = False

    while running:
        for event in pygame.event.get():
            print("PLAYER1 CLICKED ", player1_clicked)
            print("PLAYER2 CLICKED ", player2_clicked)
            if(find_solution_set):
                solution_set = model.find_a_set(displayed_cards)
                find_solution_set == False
            if(len(deck) == 0 and len(solution_set) == 0):
                display_end_game(surface, total_score)

            if((player1_clicked == False and player2_clicked == False) or clicks < 3):
                if(print_solution_set_once == False):
                    print_solution_set_once = True
                    print()
                    print("solution set")
                    print(solution_set)
                    print()
                    print("size of deck", len(deck))
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    no_set_rect = pygame.Rect(30,605,240,100)
                    get_hint_rect = pygame.Rect(430,605,240,100)
                    player1_rect = pygame.Rect(675,200,316,98)
                    player2_rect = pygame.Rect(675,400,316,98)

                    if(no_set_rect.collidepoint(pos) and solution_set == [] and len(deck) > 0):
                        displayed_cards = reset_board(surface, deck, displayed_cards, image_list, total_score)
                        find_solution_set = True
                    elif(no_set_rect.collidepoint(pos)):
                        print("====CLICKED NO SET RECT AND THERE IS A SET====")
                    elif(get_hint_rect.collidepoint(pos)):
                        if(solution_set != []):
                            clicks += 1
                            click_card_in_set(surface, image_list, displayed_cards, solution_set, clicked_images)

                    else:
                        clicked_player = False
                        if(not single_player):
                            if(player1_rect.collidepoint(pos) and not player1_clicked and not player2_clicked):
                                player1_clicked = True
                                make_player_clicked(675,200,316,98,surface, player1_clicked, player2_clicked)
                                clicked_player = True
                            elif(player2_rect.collidepoint(pos) and not player2_clicked and not player1_clicked):
                                player2_clicked = True
                                make_player_clicked(675,400,316,98,surface, player1_clicked, player2_clicked)
                                clicked_player = True
                            elif(player1_rect.collidepoint(pos) and player1_clicked):
                                make_player_unclicked(675,200,316,98,surface, player1_clicked, player2_clicked)
                                player1_clicked = False
                                clicked_player = True
                            elif(player2_rect.collidepoint(pos) and player2_clicked):
                                make_player_unclicked(675,400,316,98,surface, player1_clicked, player2_clicked)
                                player2_clicked = False
                                clicked_player = True
                        if(clicked_player == False):
                            for key, value in displayed_cards.items():
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
                    print()
                    print("is a set")
                    print()
                    if(single_player):
                        total_score += 1
                    else:
                        if(player1_clicked):
                            player1_score += 1
                        else:
                            player2_score += 1
                    list_of_rect = []
                    for card in clicked_images:
                        list_of_rect.append(get_rect_of_card(card, displayed_cards))
                        set_of_removed_cards.add(card)
                        displayed_cards.pop(card)
                    clicked_images = defaultdict()
                    if(len(deck) != 0):
                        model.add_three_new_cards(deck, displayed_cards, list_of_rect)
                    if(single_player):
                        display_cards_later(displayed_cards, image_list, surface, total_score, len(deck), single_player, player1_score, player2_score)
                    elif(player1_clicked):
                        display_cards_later(displayed_cards, image_list, surface, player1_score, len(deck), single_player, player1_score, player2_score)
                        player1_clicked = False
                    else:
                        display_cards_later(displayed_cards, image_list, surface, player2_score, len(deck), single_player, player1_score, player2_score)
                        player2_clicked = False
                    find_solution_set = True

                else:
                    print("is not a set")
                    clicked_images = defaultdict()
                    display_cards_later(displayed_cards, image_list, surface, total_score, len(deck), single_player, player1_score, player2_score)
                    player1_clicked = False
                    player2_clicked = False


        pygame.display.flip()


    pygame.quit()


if __name__ == '__main__':
	run()
