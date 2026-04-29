import random as r

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
cards = []

for x in suits:
    for y in values:
        cards.append((y, x))
# Getting a Deck of Cards

yn = int(input("Would you like to shuffle the cards 0 - No, 1 - Yes: "))
if yn:
    r.shuffle(cards)

# Giving the cards to the user and opponent, adding manual card assigning later
my_deck = []
opp_deck = []

for card in range(2):
    my_deck.append(cards.pop())
    opp_deck.append(cards.pop())

print(my_deck)
print(opp_deck)

sims = 10000
rankings = ["RF", "SF", "FK", "FH", "FL", "ST", "TK", "TP", "OP", "HC"]
table = []
my_win = 0
opp_win = 0
tie = 0

for x in range(5):
    table.append(cards.pop())
    # Analyzing the combination of my_deck
    # Analyzing the combination of opp_deck
    # Finding the better combination
    # Calculating success rates and tie rates



