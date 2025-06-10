from Platformer import jumper
from BlockPuzzle import block

def play_game():
    current_game = jumper.Jumper()
    current_game.run_carnival()
    print(current_game.minigame_to_play)
    if current_game.minigame_to_play == 'puzzle':
        play_puzzle()

def play_puzzle():
    block.run_puzzle()
    play_game()

def play_card():
    pass

def play_dart():
    pass

play_game()