# from game import Game


class Player:
    def __init__(self, name):
        self.hands = []
        self.name = name

    def draw(self, game, n=2):
        """draw cards
        @param n: the number of cards to draw
        @param game: Game instance now playing
        """
        for _ in range(n):
            self.hands.append(game.cards.pop())
        game.shuffle_cards()

    def set_name(self, name):
        self.name = name

    def put_card(self, line, cards_index):
        card = self.hands.pop(cards_index)
        if line.valid_stack(card):
            line.stack_on(card)
        else:
            self.hands.append(card)
            raise Exception

    def show_hands(self):
        # print(f'\r{self.hands}', end='')
        print(f'{self.hands}')

    def __str__(self):
        return self.name
