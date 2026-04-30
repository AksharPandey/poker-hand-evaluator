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
            continue

        values = []
        for card in combo:
            values.append(card[0])

        if set(values) == {10, 11, 12, 13, 14}:
            return x

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
            continue

        values = []
        for card in combo:
            values.append(card[0])

        values.sort()
        special_case = values == [2, 3, 4, 5, 14]
        consecutive_or_nah = values == list(range(values[0], values[-1]+1))
        if consecutive_or_nah and not special_case:
            return x
        elif special_case:
            return x
    return False


def four_of_a_kind(deck, table):
    cards = deck + table
    combinations1 = list(combinations(cards, 5))
    for x in combinations1:
        combo = list(x)
        value = []
        for card in combo:
            value.append(card[0])
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for val in values:
            count = value.count(val)
            if count == 4:
                return x
    return False

def full_house(deck, table):
    cards = deck + table
    combinations1 = list(combinations(cards, 5))
    for x in combinations1:
        combo = list(x)
        value = []
        for card in combo:
            value.append(card[0])

        if len(set(value)) > 2:
            continue

        rank_count = []
        for rank in set(value):
            rank_count.append(value.count(rank))

        if rank_count in [[3, 2], [2, 3]]:
            return x

    return False


def flush(deck, table):
    cards = deck + table
    combinations1 = list(combinations(cards, 5))
    for x in combinations1:
        combo = list(x)
        suits = []
        for z in combo:
            suits.append(z[1])

        if len(set(suits)) == 1:
            return x

    return False


def straight(deck, table):
    cards = deck + table
    combinations1 = list(combinations(cards, 5))
    for x in combinations1:
        combo = list(x)
        values = []
        for card in combo:
            values.append(card[0])

        values.sort()

        if values == list(range(values[0], values[-1]+1)):
            return x
        elif values in [[2, 3, 4, 5, 14], [10, 11, 12, 13, 14]]:
            return x

    return False


def three_of_a_kind(deck, table):
    cards = deck + table
    combinations1 = list(combinations(cards, 5))
    for x in combinations1:
        combo = list(x)
        value = []
        for card in combo:
            value.append(card[0])
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for val in values:
            count = value.count(val)
            if count == 3:
                return x

    return False


def two_pair(deck, table):
    cards = deck + table
    combinations1 = list(combinations(cards, 5))
    for x in combinations1:
        combo = list(x)
        value = []

        for card in combo:
            value.append(card[0])

        rank_count = []
        for rank in set(value):
            rank_count.append(value.count(rank))

        if rank_count in [[2, 2, 1], [1, 2, 2], [2, 1, 2]]:
            return x

    return False


def one_pair(deck, table):
    cards = deck + table
    combinations1 = list(combinations(cards, 5))
    for x in combinations1:
        combo = list(x)
        value = []
        for card in combo:
            value.append(card[0])
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for val in values:
            count = value.count(val)
            if count == 2:
                return x

    return False

def high_card(deck, table):
    cards = deck + table
    combinations1 = list(combinations(cards, 5))
    best_combo = None
    for x in combinations1:
        combo = list(x)
        if not(best_combo):
            best_combo = x

        elif x > best_combo:
            best_combo = x

    return best_combo



