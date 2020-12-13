import random
from player import Player
from lines import AscLine, DescLine


class Game:

    def __init__(self, player_n=2):
        self.player_names = ['A', 'B', 'C', 'D', 'E']
        self.cards_used = 0
        self.cards = [x for x in range(2, 100)] * 2
        self.players_count = player_n
        self.set_holds()
        self.set_lines()
        self.turn = 0
        self.player_index = 0
        self.playing = False
        self.min_cards = 2

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def set_holds(self):
        players_count = self.players_count
        if players_count == 1:
            holds = 8
        elif players_count == 2:
            holds = 7
        elif players_count > 2 and players_count <= 5:
            holds = 6
        else:
            print('**Check Players (max 5)**')
            holds = 0
        self.holds = holds

    def set_players(self):
        self.players = []
        for _ in range(self.players_count):
            self.players.append(Player(self.player_names.pop(0)))
        self.now_player = self.players[0]

    def handout(self):
        # Cards distribution
        for player in self.players:
            for _ in range(self.holds):
                player.hands.append(self.cards.pop())

    def show_players_hands(self):
        for player in self.players:
            print(f'{player.name} - {player.hands}')

    def set_lines(self):
        # Table setting
        self.asc1 = AscLine()
        self.asc2 = AscLine()
        self.desc1 = DescLine()
        self.desc2 = DescLine()
        self.lines = [self.asc1, self.asc2, self.desc1, self.desc2]

    def show_lines_top(self):
        print(f'asc1 >> {self.asc1.top}')
        print(f'asc2 >> {self.asc2.top}')
        print(f'desc1 >> {self.desc1.top}')
        print(f'desc2 >> {self.desc2.top}')

    def next_turn(self):
        self.turn += 1
        self.player_index = self.turn % self.players_count
        print(f'next turn >> {self.players[self.player_index]}')

    def game_start(self):
        self.playing = True

    def game_end(self):
        self.playing = False

    def check_deck_empty(self):
        if not self.cards:
            self.min_cards = 1
            return True
        return False

    def player_do(self, game, player_index):
        player = self.players[player_index]
        cards_used = 0
        while self.playing:
            if not self.check_end(player_index):
                print('playing')
                self.show_lines_top()
                player.show_hands()
                n = int(input('which card do you want to put on?'))
                line_index = int(input('which line do you want to put on?'))
                line = self.lines[line_index]
                player.put_card(line, n)
                cards_used += 1
                # when cards_used > min_cards and player want to stop
                break
            else:
                print('finish')
                self.playing = False
        player.draw(game, cards_used)

    def check_end(self, player_index):
        for card in self.players[player_index].hands:
            if (
                self.asc1.top < card or
                self.asc2.top < card or
                self.desc1.top > card or
                self.desc2. top > card
            ):
                return False
        return True

    # def play(self):
    #     # End condition
    #     while not self.is_end():
    #         for id in range(len(self.players)):
    #             self.turn_do(id)
    #     print('Game Finished')

    # def is_end(self):
    #     if self.cards or self.cards_onHands:
    #         for onHand in self.cards_onHands:
    #             try:
    #                 for card in onHand:
    #                     if card < self.desc1 or card < self.desc2 or card > self.asc1 or card > self.asc2:
    #                         return False
    #             except:
    #                 continue

    #     return True

    # def turn_do(self, id):
    #     self.turn_message(id)
    #     while not self.end_player(id):
    #         print(self.cards_onHands[id])
    #         if self.cards_used < 2:
    #             self.selected = int(
    #                 input('Select a card(put the card number): '))
    #         else:
    #             msg = "Select a card(put the card number) or End turn with '0': "
    #             self.selected = int(input(msg))
    #         print('*'*50)
    #         if self.selected in self.cards_onHands[id]:
    #             self.card_index = self.cards_onHands[id].index(self.selected)
    #             self.now_card = self.cards_onHands[id].pop(self.card_index)
    #             while True:
    #                 self.card_at = self.card_dest()
    #                 if self.put_card_on(self.card_at):
    #                     break

    #         # End turn phase
    #         elif self.selected == 0 and self.cards_used >= 2:
    #             print('Turn finished')
    #             self.cards_used = 0
    #             self.draw_cards(id)
    #             break
    #         else:
    #             print('**Put the number correctly**')

    # def end_player(self, id):
    #     if len(self.cards_onHands[id]) > self.holds - 2:
    #         for card in self.cards_onHands[id]:
    #             if card > self.desc1 or card > self.desc2 or card < self.asc1 or card < self.asc2:
    #                 print(f'Player {self.players[id]} out')
    #                 return True
    #     return False

    # def turn_message(self, id):
    #     print('*'*50)
    #     print(f'Turn of Player {self.players[id]}')
    #     print('*'*50)
    #     print(self.cards_onHands[id])
    #     print()
    #     self.status_message()

    # def status_message(self):
    #     self.cards_left = len(self.cards)
    #     print(f'{self.cards_left} cards left ')
    #     self.table_status = f'(1)asc1:  {self.asc1:2} (2)asc2:  {self.asc2:2} \n(3)desc1: {self.desc1:2} (4)desc2: {self.desc2:2}'
    #     print(self.table_status)

    # def card_dest(self):
    #     while True:
    #         print(f'Where do you want to put {self.now_card} on?')
    #         print('*'*50)
    #         print(self.table_status)
    #         self.dest = int(input('Type the number: '))
    #         print('*'*50)
    #         if self.dest > 4 or self.dest < 1:
    #             print('**Type right line number(1 ~ 4)**')
    #             continue
    #         return self.dest

    # def put_card_on(self, dest):
    #     if dest == 1:
    #         if self.asc1 < self.now_card or self.asc1 - 10 == self.now_card:
    #             self.asc1 = self.now_card
    #         else:
    #             print('***Wrong way.. think again***')
    #             return False
    #     elif dest == 2:
    #         if self.asc2 < self.now_card or self.asc2 - 10 == self.now_card:
    #             self.asc2 = self.now_card
    #         else:
    #             print('Wrong way.. think again')
    #             return False
    #     elif dest == 3:
    #         if self.desc1 > self.now_card or self.desc1 + 10 == self.now_card:
    #             self.desc1 = self.now_card
    #         else:
    #             print('Wrong way.. think again')
    #             return False
    #     elif dest == 4:
    #         if self.desc2 > self.now_card or self.desc2 + 10 == self.now_card:
    #             self.desc2 = self.now_card
    #         else:
    #             print('Wrong way.. think again')
    #             return False

    #     self.now_card = 0
    #     self.cards_used += 1
    #     self.status_message()
    #     return True

    # def draw_cards(self, id):
    #     while len(self.cards_onHands[id]) < self.holds:
    #         self.cards_onHands[id].append(self.cards.pop())
    #     self.cards_onHands[id].sort()
