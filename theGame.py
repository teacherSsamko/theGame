import random

# 2 ~ 98 number cards
# two ascending lines & two descending lines
# Hold 7 cards each when players are two.
# Player must draw more than 2 cards at each turn.


class TheGame:
    def __init__(self):
        self.set_cards()
        self.handout()
        self.set_table()
        self.drawed = 0
        self.turn_over = False
        self.turn_do()

    def set_cards(self):
        self.cards = []
        for i in range(2, 99):
            self.cards.append(i)
        random.shuffle(self.cards)

    def handout(self):
        # Cards distribution
        self.playerA = []
        self.playerB = []
        self.holds = 7

        for i in range(self.holds):
            self.playerA.append(self.cards.pop())
            self.playerB.append(self.cards.pop())
        self.playerA.sort()
        self.playerB.sort()
        print(self.playerA)
        print(self.playerB)

    def set_table(self):
        # Table setting
        self.asc1 = 1
        self.asc2 = 1
        self.desc1 = 99
        self.desc2 = 99
        self.status_message()

    def turn_do(self):
        self.turn_message()

        while not self.turn_over:
            if self.drawed < 2:
                self.selected = int(
                    input('Select a card(put the card number): '))
            else:
                self.selected = int(
                    input("Select a card(put the card number) or end turn with '0': "))
            print('*'*50)
            if self.selected in self.playerA:
                self.card_index = self.playerA.index(self.selected)
                self.now_card = self.playerA.pop(self.card_index)
                self.card_at = self.card_dest()
                self.put_card_on(self.card_at)

            # End turn phase
            elif self.selected == 0 and self.drawed >= 2:
                print('Turn finished')
                self.drawed = 0
                self.turn_over = True
                break
            else:
                print('**Put the number correctly**')

    def turn_message(self):
        print('*'*50)
        print('Turn of Player A')
        print('*'*50)
        print(self.playerA)
        print()
        self.status_message()

    def status_message(self):
        self.cards_left = len(self.cards)
        print(f'{self.cards_left} cards left ')
        self.table_status = f'(1)asc1:  {self.asc1:2} (2)asc2:  {self.asc2:2} \n(3)desc1: {self.desc1:2} (4)desc2: {self.desc2:2}'
        print(self.table_status)

    def card_dest(self):
        while True:
            print(f'Where do you want to put {self.now_card} on?')
            print('*'*50)
            print(self.table_status)
            self.dest = int(input('Type the number: '))
            print('*'*50)
            if self.dest > 4 or self.dest < 1:
                print('**Type right line number(1 ~ 4)**')
                continue
            return self.dest

    def put_card_on(self, dest):
        if dest == 1:
            self.asc1 = self.now_card
        elif dest == 2:
            self.asc2 = self.now_card
        elif dest == 3:
            self.desc1 = self.now_card
        elif dest == 4:
            self.desc2 = self.now_card

        self.now_card = 0
        self.drawed += 1
        self.status_message()


TheGame()
