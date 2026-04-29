import numpy as np
from itertools import combinations

def royal_flush(deck, table):
    cards = deck + table
    combinations1 = list(combinations(cards, 5))
    for x in combinations1:
        combo = list(x)
        suit = []
        for card in combo:
            if card[1] in suit:
                pass
            else:
                suit.append(card[1])

        if len(suit) > 1:
            return False

        values = []
        for card in combo:
            values.append(card[0])

        if set(values) == {10, 11, 12, 13, 14}:
            return True

    return False


def straight_flush(deck, table):
    cards = deck + table
    combinations1 = list(combinations(cards, 5))
    for x in combinations1:
        combo = list(x)
        suit = []
        for card in combo:
            if card[1] in suit:
                pass
            else:
                suit.append(card[1])

        if len(suit) > 1:
            return False

        values = []
        for card in combo:
            values.append(card[0])

        values.sort()
        special_case = values == [2, 3, 4, 5, 14]
        consecutive_or_nah = values == list(range(values[0], values[-1]+1))
        if consecutive_or_nah and not special_case:
            return True
        elif special_case:
            return True
    return False

def four_of_a_kind(deck, table):
    cards = deck + table
    combinations1 = list(combinations(cards, 5))
    for x in combinations1:
        combo = list(x)
        value = []
        for card in combo:
            value.append(card[0])













    return False

def straight_flush(deck, table):
