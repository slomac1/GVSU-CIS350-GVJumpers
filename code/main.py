from Platformer import jumper
from BlockPuzzle import block

def play_game():
    current_game = jumper.Jumper()
    current_game.run_carnival()
    if current_game.minigame_to_play == 'puzzle':
        play_puzzle()

def play_puzzle():
    block.run_puzzle()
    play_game()

play_game()