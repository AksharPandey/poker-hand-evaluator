import random as r
import Ranking_Functions as rf
import matplotlib.pyplot as plt

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
cards = []

for x in suits:
    for y in values:
        cards.append((y, x))

# Getting a Deck of Cards
r.shuffle(cards)

# Giving the cards to the user and opponent, adding manual card assigning later
deck1 = []
deck2 = []

ask = input("Do you wanna randomly generate opponent and your cards  (y/n): ")
if ask == 'n':
    value1 = int(input("Enter value for your card1 (1-14), where J - 11, Q - 12, K - 13, A - 14: "))
    suit1 = input("Enter suit for your card1 (Spades, Hearts, Diamonds, Clubs): ")
    value2 = int(input("Enter value for your card2 (1-14), where J - 11, Q - 12, K - 13, A - 14: "))
    suit2 = input("Enter suit for your card2 (Spades, Hearts, Diamonds, Clubs): ")

    value3 = int(input("Enter value for opp card1 (1-14), where J - 11, Q - 12, K - 13, A - 14: "))
    suit3 = input("Enter suit for opp card1 (Spades, Hearts, Diamonds, Clubs): ")
    value4 = int(input("Enter value for opp card2 (1-14), where J - 11, Q - 12, K - 13, A - 14: "))
    suit4 = input("Enter suit for opp card2 (Spades, Hearts, Diamonds, Clubs): ")

    deck1.append((value1, suit1))
    deck1.append((value2, suit2))
    deck2.append((value3, suit3))
    deck2.append((value4, suit4))

else:
    for card in range(2):
        deck1.append(cards.pop())
        deck2.append(cards.pop())

D1 = str(deck1[0][0]) + ' of ' + deck1[0][1] + '/' + str(deck1[1][0]) + ' of ' + deck1[1][1]
D2 = str(deck2[0][0]) + ' of ' + deck2[0][1] + '/' + str(deck2[1][0]) + ' of ' + deck2[1][1]
print(D1)
print(D2)

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
            ranks1.sort(reverse=True)
            ranks2.sort(reverse=True)
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
            ranks1 = []
            ranks2 = []
            for rank, suits in strongest_hand1:
                ranks1.append(rank)
            for rank, suits in strongest_hand2:
                ranks2.append(rank)

            trip_rank1 = 0
            trip_rank2 = 0
            for z in ranks1:
                if ranks1.count(z) == 3:
                    trip_rank1 = z
                    break
            for z in ranks2:
                if ranks2.count(z) == 3:
                    trip_rank2 = z
                    break

            pair_rank1 = 0
            pair_rank2 = 0
            if trip_rank1 > trip_rank2:
                deck1_win += 1
            elif trip_rank2 == trip_rank1:
                for z in ranks1:
                    if ranks1.count(z) == 1:
                        pair_rank1 = z
                        break
                for z in ranks2:
                    if ranks2.count(z) == 1:
                        pair_rank2 = z
                        break
                if pair_rank2 > pair_rank1:
                    deck2_win += 1
                elif pair_rank2 == pair_rank1:
                    tie += 1
                else:
                    deck1_win += 1
            else:
                deck2_win += 1

        elif rank1 == 'FL' and rank2 == 'FL':
            ranks1 = []
            ranks2 = []
            for rank, suits in strongest_hand1:
                ranks1.append(rank)
            for rank, suits in strongest_hand2:
                ranks2.append(rank)
            ranks1.sort(reverse=True)
            ranks2.sort(reverse=True)
            if ranks1 > ranks2:
                deck1_win +=1
            elif ranks1 == ranks2:
                tie += 1
            else:
                deck2_win += 1

        elif rank1 == 'ST' and rank2 == 'ST':
            ranks1 = []
            ranks2 = []
            for rank, suits in strongest_hand1:
                ranks1.append(rank)
            for rank, suits in strongest_hand2:
                ranks2.append(rank)
            ranks1.sort(reverse=True)
            ranks2.sort(reverse=True)

            if ranks1 == [14, 5, 4, 3, 2]:
                ranks1 = [5, 4, 3, 2, 1]
            if ranks2 == [14, 5, 4, 3, 2]:
                ranks2 = [5, 4, 3, 2, 1]

            if ranks1 > ranks2:
                deck1_win +=1
            elif ranks1 == ranks2:
                tie += 1
            else:
                deck2_win += 1

        elif rank1 == 'TK' and rank2 == 'TK':
            ranks1 = []
            ranks2 = []
            for rank, suits in strongest_hand1:
                ranks1.append(rank)
            for rank, suits in strongest_hand2:
                ranks2.append(rank)

            trip_rank1 = 0
            trip_rank2 = 0
            for z in ranks1:
                if ranks1.count(z) == 3:
                    trip_rank1 = z
                    break
            for z in ranks2:
                if ranks2.count(z) == 3:
                    trip_rank2 = z
                    break

            if trip_rank1 > trip_rank2:
                deck1_win += 1
            elif trip_rank2 == trip_rank1:
                two_rank1 = []
                two_rank2 = []
                for z in ranks1:
                    if z != trip_rank1:
                        two_rank1.append(z)
                for z in ranks2:
                    if z != trip_rank2:
                        two_rank2.append(z)

                two_rank1.sort(reverse=True)
                two_rank2.sort(reverse=True)

                if two_rank1 > two_rank2:
                    deck1_win += 1
                elif two_rank1 == two_rank2:
                    tie += 1
                else:
                    deck2_win += 1

            else:
                deck2_win += 1

        elif rank1 == 'TP' and rank2 == 'TP':
            ranks1 = []
            ranks2 = []
            for rank, suits in strongest_hand1:
                ranks1.append(rank)
            for rank, suits in strongest_hand2:
                ranks2.append(rank)

            pair_rank1 = []
            pair_rank2 = []
            kicker_rank1 = 0
            kicker_rank2 = 0
            for z in ranks1:
                if ranks1.count(z) == 2:
                    if not (z in pair_rank1):
                        pair_rank1.append(z)
                else:
                    kicker_rank1 = z

            for z in ranks2:
                if ranks2.count(z) == 2:
                    if not (z in pair_rank2):
                        pair_rank2.append(z)
                else:
                    kicker_rank2 = z

            pair_rank2.sort(reverse=True)
            pair_rank1.sort(reverse=True)

            if pair_rank2 > pair_rank1:
                deck2_win += 1
            elif pair_rank1 == pair_rank2:
                if kicker_rank1 > kicker_rank2:
                    deck1_win += 1
                elif kicker_rank2 == kicker_rank1:
                    tie += 1
                else:
                    deck2_win += 1
            else:
                deck1_win += 1

        elif rank1 == 'OP' and rank2 == 'OP':
            ranks1 = []
            ranks2 = []
            for rank, suits in strongest_hand1:
                ranks1.append(rank)
            for rank, suits in strongest_hand2:
                ranks2.append(rank)

            pair_rank1 = 0
            kicker_rank1 = []
            pair_rank2 = 0
            kicker_rank2 = []

            for z in ranks1:
                if ranks1.count(z) == 2:
                    pair_rank1 = z
                else:
                    kicker_rank1.append(z)
            for z in ranks2:
                if ranks2.count(z) == 2:
                    pair_rank2 = z
                else:
                    kicker_rank2.append(z)

            kicker_rank1.sort(reverse=True)
            kicker_rank2.sort(reverse=True)

            if pair_rank1 > pair_rank2:
                deck1_win += 1

            elif pair_rank1 == pair_rank2:
                if kicker_rank1 > kicker_rank2:
                    deck1_win += 1
                elif kicker_rank2 > kicker_rank1:
                    deck2_win += 1
                else:
                    tie += 1
            else:
                deck2_win += 1

        elif rank1 == 'HC' and rank2 == 'HC':
            ranks1 = []
            ranks2 = []
            for rank, suits in strongest_hand1:
                ranks1.append(rank)
            for rank, suits in strongest_hand2:
                ranks2.append(rank)

            ranks1.sort(reverse=True)
            ranks2.sort(reverse=True)

            if ranks1 > ranks2:
                deck1_win += 1
            elif ranks2 > ranks1:
                deck2_win += 1
            else:
                tie += 1

    else:
        deck1_win += 1



deck1_win_percent = (deck1_win * 100) / sims
deck2_win_percent = (deck2_win * 100) / sims
tie_percent = (tie * 100) / sims

D1 = str(deck1[0][0]) + ' of ' + deck1[0][1] + '/' + str(deck1[1][0]) + ' of ' + deck1[1][1]
D2 = str(deck2[0][0]) + ' of ' + deck2[0][1] + '/' + str(deck2[1][0]) + ' of ' + deck2[1][1]

print(D1, "wins", deck1_win_percent, "% of times")
print(D2, "wins", deck2_win_percent, "% of times")
print("Game ties", tie_percent, "% of times")

value = [deck1_win_percent, tie_percent, deck2_win_percent]
name = [D1, 'Tie', D2]
color = ['green', 'grey', 'red']

plt.bar(name, value, color=color)
plt.show()












