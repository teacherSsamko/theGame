"""
2 ~ 98 number cards
two ascending lines & two descending lines
Hold 7 cards each when players are two.
Player must draw more than 2 cards at each turn.
"""
from game import Game
from player import Player

if __name__ == "__main__":
    game = Game()
    game.shuffle_cards()
    game.set_players()
    game.handout()
    game.show_lines_top()
    game.show_players_hands()
    game.game_start()
    while game.playing:
        game.player_do(game, game.player_index)
        game.next_turn()
