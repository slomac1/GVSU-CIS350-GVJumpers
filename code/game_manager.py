from Platformer import jumper
from BlockPuzzle import block
from DartGame import darts
from Blackjack import blackjack

class GameManager:
    def play_game(self):
        current_game = jumper.Jumper()
        current_game.run_carnival()
        if current_game.minigame_to_play == 'puzzle':
            self.play_block()
        elif current_game.minigame_to_play == 'darts':
            self.play_dart()
        elif current_game.minigame_to_play == 'cards':
            self.play_blackjack()
        return

    def play_block(self):
        current_game = block.Puzzle()
        current_game.run_puzzle()
        self.play_game()

    def play_blackjack(self):
        blackjack.play_game_gui()
        self.play_game()

    def play_dart(self):
        current_game = darts.Darts()
        current_game.play_darts()
        self.play_game()

if __name__ == '__main__':
    new_game = GameManager()
    new_game.play_game()