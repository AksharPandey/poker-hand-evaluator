import random as r
import Ranking_Functions as rf

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
cards = []

for x in suits:
    for y in values:
        cards.append((y, x))
# Getting a Deck of Cards

yn = int(input("Would you like to shuffle the cards 0 - No, 1 - Yes: "))
if yn:
    r.shuffle(cards)

# Giving the cards to the user and opponent, adding manual card assigning later
deck1 = []
deck2 = []

for card in range(2):
    deck1.append(cards.pop())
    deck2.append(cards.pop())

print(deck1)
print(deck2)

sims = int(input("Enter amount of simulations: "))
rankings = ["RF", "SF", "FK", "FH", "FL", "ST", "TK", "TP", "OP", "HC"]
deck1_win = 0
deck2_win = 0
tie = 0


for x in range(sims):
    table = []
    r.shuffle(cards)
    for num in range(5):
        table.append(cards[num])

    if rf.royal_flush(deck1, table):
        rank1 = 'RF'
        strongest_hand1 = rf.royal_flush(deck1, table)
    elif rf.straight_flush(deck1, table):
        rank1 = 'SF'
        strongest_hand1 = rf.straight_flush(deck1, table)
    elif rf.four_of_a_kind(deck1, table):
        rank1 = 'FK'
        strongest_hand1 = rf.four_of_a_kind(deck1, table)
    elif rf.full_house(deck1, table):
        rank1 = 'FH'
        strongest_hand1 = rf.full_house(deck1, table)
    elif rf.flush(deck1, table):
        rank1 = 'FL'
        strongest_hand1 = rf.flush(deck1, table)
    elif rf.straight(deck1, table):
        rank1 = 'ST'
        strongest_hand1 = rf.straight(deck1, table)
    elif rf.three_of_a_kind(deck1, table):
        rank1 = 'TK'
        strongest_hand1 = rf.three_of_a_kind(deck1, table)
    elif rf.two_pair(deck1, table):
        rank1 = 'TP'
        strongest_hand1 = rf.two_pair(deck1, table)
    elif rf.one_pair(deck1, table):
        rank1 = 'OP'
        strongest_hand1 = rf.one_pair(deck1, table)
    else:
        rank1 = 'HC'
        strongest_hand1 = rf.high_card(deck1, table)

    if rf.royal_flush(deck2, table):
        rank2 = 'RF'
        strongest_hand2 = rf.royal_flush(deck2, table)
    elif rf.straight_flush(deck2, table):
        rank2 = 'SF'
        strongest_hand2 = rf.straight_flush(deck2, table)
    elif rf.four_of_a_kind(deck2, table):
        rank2 = 'FK'
        strongest_hand2 = rf.four_of_a_kind(deck2, table)
    elif rf.full_house(deck2, table):
        rank2 = 'FH'
        strongest_hand2 = rf.full_house(deck2, table)
    elif rf.flush(deck2, table):
        rank2 = 'FL'
        strongest_hand2 = rf.flush(deck2, table)
    elif rf.straight(deck2, table):
        rank2 = 'ST'
        strongest_hand2 = rf.straight(deck2, table)
    elif rf.three_of_a_kind(deck2, table):
        rank2 = 'TK'
        strongest_hand2 = rf.three_of_a_kind(deck2, table)
    elif rf.two_pair(deck2, table):
        rank2 = 'TP'
        strongest_hand2 = rf.two_pair(deck2, table)
    elif rf.one_pair(deck2, table):
        rank2 = 'OP'
        strongest_hand2 = rf.one_pair(deck2, table)
    else:
        rank2 = 'HC'
        strongest_hand2 = rf.high_card(deck2, table)

    if rankings.index(rank1) > rankings.index(rank2):
        deck2_win += 1

    elif rank1 == rank2:
        if rank1 == 'RF' and rank2 == 'RF':
            tie += 1
        elif rank1 == 'SF' and rank2 == 'SF':
            ranks1 = []
            ranks2 = []
            for rank, suits in strongest_hand1:
                ranks1.append(rank)
            for rank, suits in strongest_hand2:
                ranks2.append(rank)
            ranks1.sort()
            ranks2.sort()
            if ranks1 > ranks2:
                deck1_win +=1
            elif ranks1 == ranks2:
                tie += 1
            else:
                deck2_win += 1

        elif rank1 == 'FK' and rank2 == 'FK':
            ranks1 = []
            ranks2 = []
            for rank, suits in strongest_hand1:
                ranks1.append(rank)
            for rank, suits in strongest_hand2:
                ranks2.append(rank)

            quad_rank1 = 0
            quad_rank2 = 0
            for z in ranks1:
                if ranks1.count(z) == 4:
                    quad_rank1 = z
                    break
            for z in ranks2:
                if ranks2.count(z)==4:
                    quad_rank2 = z
                    break

            kicker_rank1 = 0
            kicker_rank2 = 0
            if quad_rank1 > quad_rank2:
                deck1_win += 1
            elif quad_rank2 == quad_rank1:
                for z in ranks1:
                    if ranks1.count(z) == 1:
                        kicker_rank1 = z
                        break
                for z in ranks2:
                    if ranks2.count(z) == 1:
                        kicker_rank2 = z
                        break
                if kicker_rank2 > kicker_rank1:
                    deck2_win += 1
                elif kicker_rank2 == kicker_rank1:
                    tie += 1
                else:
                    deck1_win += 1
            else:
                deck2_win += 1

        elif rank1 == 'FH' and rank2 == 'FH':
            tie += 1
        elif rank1 == 'FL' and rank2 == 'FL':
            tie += 1
        elif rank1 == 'ST' and rank2 == 'ST':
            tie += 1
        elif rank1 == 'TK' and rank2 == 'TK':
            tie += 1
        elif rank1 == 'TP' and rank2 == 'TP':
            tie += 1
        elif rank1 == 'OP' and rank2 == 'OP':
            tie += 1
        elif rank1 == 'HC' and rank2 == 'HC':
            tie += 1

    else:
        deck1_win += 1



deck1_win_percent = (deck1_win * 100) / sims
deck2_win_percent = (deck2_win * 100) / sims
tie_percent = (tie * 100) / sims

print("Deck1 wins", deck1_win_percent, "percent of times")
print("Deck2 wins", deck2_win_percent, "percent of times")
print("Game ties", tie_percent, "percent of times")










