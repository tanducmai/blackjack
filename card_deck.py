#
# card_deck module - PSP Assignment 2, 2021.
# DO NOT MODIFY!
#

import random


# Contains cards in the format [value, suit]
# DO NOT ACCESS THIS VARIABLE!
# Call draw_card() instead.
deck = []


def draw_card():
    '''
    Removes and returns the last item from the global deck.
    The deck will be reset after the last card is drawn.
    '''
    global deck
    if len(deck) == 0:
        fill(deck)
    return deck.pop()


def fill(deck):
    '''
    DO NOT call this function.
    This function is called automatically by draw_card().
    Creates and returns a new deck of 52 cards.
    Each card is a list in the format [value, suit] e.g., ['Ace', 'Spades'].
    '''
    deck.clear()
    for val in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
        for suit in ['Hearts', 'Spades', 'Diamonds', 'Clubs']:
            deck.append([val, suit])
    random.shuffle(deck)


