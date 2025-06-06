# Overview
This document contains our software requirment specifications. 

# Functional Requirements
1. Platformer
    1. The player shall be able to move left, right and jump barring any obstacles.
    2. The user interface shall show important character data such as health, currency and objectives.
    3. The player shall be able to interact with objects in the world, including NPC characters and enemies. 
2. Darts
    1. There shall be a dart board.
    2. There shall be different point values associated to sections of the dart board. 
    3. There shall be a circle to indicate where the dart will land.
3. Game 2
    1. There will be a board.
    2. The board will have different-sized blocks in it, and a square red block.
    3. There will be slit at one side, where red block should leave.
4. Blackjack Card Game
    1. The player shall be able to place a wager into the game
    2. The Player shall have game options to hit, stand, split, or double down in the game.
    3. The game shall be able to deal out a hand and correctly determine the winner of the hand.
5. The background color for all mini-games shall have an RGB value of 0x000000 or 0x000000. (not sure what colors yet - feel free to edit).

# Non-Functional Requirements 
1. Platformer
    1. The controls shall be easy to understand and accessible at any time.
    2. The user shall be able to adjust FPS, Window size within a setting menu.
    3. The game shall be able to run on any desktop platform.
2. Darts 
    1. There shall be 15 darts.
    2. The dart shall land within 3 seconds of "throwing" it.
    3. If the dart causes the score to drop below zero, it shall be invalid. 
3. Game 2
    1. The game will be 1 minute. 
    2. The player will have 3 tries.
    3. Each try will have set points.
4. Blackjack Card Game
    1. The game shall not display entry options that don't make sense for the current situation in the game
    2. The user shall be able to quit playing whenever they want.
    3. The user shall not be able to play with a negative credit balance
