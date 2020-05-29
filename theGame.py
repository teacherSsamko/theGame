import random

# 2 ~ 98 number cards
# two ascending lines & two descending lines
# Hold 7 cards each when players are two.
# Player must draw more than 2 cards at each turn.


class TheGame:

    def __init__(self):
        self.player = ['A', 'B', 'C', 'D', 'E']
        self.set_cards()
        self.set_players()
        self.handout()
        self.set_table()
        self.cards_used = 0
        self.play()

    def set_cards(self):
        self.cards = []
        for i in range(2, 99):
            self.cards.append(i)
        random.shuffle(self.cards)

    def set_players(self):
        self.holds = 0
        while not self.holds:
            self.players_count = int(input('How many players? (max 5)'))
            if self.players_count == 1:
                self.holds = 8
            elif self.players_count == 2:
                self.holds = 7
            elif self.players_count > 2 and self.players_count <= 5:
                self.holds = 6
            else:
                print('**Check Players (max 5)**')
                self.holds = 0
        self.players = []
        for i in range(self.players_count):
            self.players.append(self.player.pop(0))

    def handout(self):
        # Cards distribution
        self.cards_onHands = []
        for x in range(self.players_count):
            temp = []
            for i in range(self.holds):
                temp.append(self.cards.pop())
            temp.sort()
            self.cards_onHands.insert(x, temp)
        print(self.cards_onHands)

    def set_table(self):
        # Table setting
        self.asc1 = 1
        self.asc2 = 1
        self.desc1 = 99
        self.desc2 = 99
        self.status_message()

    def play(self):
        # End condition
        while not self.is_end():
            for id in range(len(self.players)):
                self.turn_do(id)
        print('Game Finished')
        print(self.cards_onHands)

    def is_end(self):
        if self.cards or self.cards_onHands:
            for onHand in self.cards_onHands:
                try:
                    for card in onHand:
                        if card < self.desc1 or card < self.desc2 or card > self.asc1 or card > self.asc2:
                            return False
                except:
                    continue

        return True

    def turn_do(self, id):
        self.turn_message(id)
        while not self.end_player(id):
            print(self.cards_onHands[id])
            if self.cards_used < 2:
                self.selected = int(
                    input('Select a card(put the card number): '))
            else:
                msg = "Select a card(put the card number) or End turn with '0': "
                self.selected = int(input(msg))
            print('*'*50)
            if self.selected in self.cards_onHands[id]:
                self.card_index = self.cards_onHands[id].index(self.selected)
                self.now_card = self.cards_onHands[id].pop(self.card_index)
                while True:
                    self.card_at = self.card_dest()
                    if self.put_card_on(self.card_at):
                        break

            # End turn phase
            elif self.selected == 0 and self.cards_used >= 2:
                print('Turn finished')
                self.cards_used = 0
                self.draw_cards(id)
                break
            else:
                print('**Put the number correctly**')

    def end_player(self, id):
        if len(self.cards_onHands[id]) > self.holds - 2:
            for card in self.cards_onHands[id]:
                if card > self.desc1 or card > self.desc2 or card < self.asc1 or card < self.asc2:
                    print(f'Player {self.players[id]} out')
                    return True
        return False

    def turn_message(self, id):
        print('*'*50)
        print(f'Turn of Player {self.players[id]}')
        print('*'*50)
        print(self.cards_onHands[id])
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
            if self.asc1 < self.now_card or self.asc1 - 10 == self.now_card:
                self.asc1 = self.now_card
            else:
                print('***Wrong way.. think again***')
                return False
        elif dest == 2:
            if self.asc2 < self.now_card or self.asc2 - 10 == self.now_card:
                self.asc2 = self.now_card
            else:
                print('Wrong way.. think again')
                return False
        elif dest == 3:
            if self.desc1 > self.now_card or self.desc1 + 10 == self.now_card:
                self.desc1 = self.now_card
            else:
                print('Wrong way.. think again')
                return False
        elif dest == 4:
            if self.desc2 > self.now_card or self.desc2 + 10 == self.now_card:
                self.desc2 = self.now_card
            else:
                print('Wrong way.. think again')
                return False

        self.now_card = 0
        self.cards_used += 1
        self.status_message()
        return True

    def draw_cards(self, id):
        while len(self.cards_onHands[id]) < self.holds:
            self.cards_onHands[id].append(self.cards.pop())
        self.cards_onHands[id].sort()


class Player:
    def __init__(self):
        self.hands = []

    def draw(self, id):
        pass


TheGame()
