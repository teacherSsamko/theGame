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
playerA.sort()
playerB.sort()
print(playerA)
print(playerB)

# Play Parts
# Table setting
asc1 = 1
asc2 = 1
desc1 = 99
desc2 = 99
table = f'(1)asc1:  {asc1:2} (2)asc2:  {asc2:2} \n(3)desc1: {desc1:2} (4)desc2: {desc2:2}'
print(table)

# Method for playing


def card_dest():
    while True:
        dest = int(input('Type the number'))
        if dest > 4 or dest < 1:
            print('Type right line number(1 ~ 4): ')
            continue
        return dest


# Select Cards
cards_left = len(cards)
drawed = 0
turnover = False
print('*'*50)
print('Turn of Player A')
print('*'*50)
print(playerA)
print()
print(table)

while not turnover:
    selected = int(input('Select a card(put the card number): '))
    if selected in playerA:
        card_index = playerA.index(selected)
        now_card = playerA.pop(card_index)
        print(f'Where do you want to put {now_card} on?')
        print(table)
        card_dest = card_dest()

        break
    else:
        print('**Put the number correctly**')
