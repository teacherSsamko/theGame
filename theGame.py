import random

# 2 ~ 98 number cards
# two ascending lines & two descending lines
# Hold 7 cards each when players are two.
# Player must draw more than 2 cards at each turn.

# Cards setting
cards = []
for i in range(2, 99):
    cards.append(i)
random.shuffle(cards)

# Cards distribution
playerA = []
playerB = []
holds = 7

for i in range(holds):
    playerA.append(cards.pop())
    playerB.append(cards.pop())
print(playerA)
print(playerB)

# Play Parts
# Table setting
asc1 = 1
asc2 = 1
desc1 = 99
desc2 = 99
table = f'asc1:  {asc1:2} asc2:  {asc2:2} \ndesc1: {desc1:2} desc2: {desc2:2}'
print(table)

# Select Cards
