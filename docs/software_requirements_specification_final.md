# Overview

This document lays out all the functional and non-functional requirements for the 4 games that make up the entiriety of the game experience. Since each games operates in significantly different parameters each one has its own unique requirments. 

# Software Requirements

The requirements are split into 4 categories for both functional and non-functional. The requirements are labeled with the format x.x.x. Where the first number represents which game the requirement is for. The second number dictates if it is a functional(1) or non-functional(2) requirement. The thrid number is which requirement it is in that category. 

## Functional Requirements

### Platformer (1.1.0)

| ID  | Requirement     | 
| :-------------: | :----------: | 
| 1.1.1 | The player shall be able to move right, left and jump.|
| 1.1.2 | The player shall remain in the center of the screen when moving and everything else shall appear to not be moving.|
| 1.1.3 | The player shall not be able to move through any non-background surfaces and should not be affected by background images. |
| 1.1.4 | The player shall be affected by gravity, pushing them down while in the air. |
| 1.1.5 | The screen shall display the players health, out of 100 in the top left corner. |
| 1.1.6 | The screen shall display how many tickets the player is currently holding in the top left corner.
| 1.1.7 | The player shall have a 4-frame animated walk while moving and not in the air.  |
| 1.1.8 | The player shall have separate still frames for jumping and standing still. |
| 1.1.9 | The player shall have an animated 5-frame attack animation that is not cancellable.  |
| 1.1.10 | The player shall be able to attack only while in the tent and the attack shall be on a 1.5 sec cooldown. |
| 1.1.11 | The tent shall have a base layout with 9 columns of scaffolding, separated by 540 pixels and 3 pieces high to support a randomly generated layout. |
| 1.1.12 | The tent shall be randomly generated every time the player enters with up to 20 medium or long balance beams and 10 enemies that only spawn on the scaffolding pieces. |
| 1.1.13 | The enemy shall automatically detect when the player is within 600 pixels in any direction and move toward the player until the player moves out of range. |
| 1.1.14 | The enemy shall deal 10 damage to the player when it comes into contact with them, and the player shall only be able to take damage once every .25 seconds. |
| 1.1.15 | Upon entering a minigame the players position, health, tickets, and the screen settings shall be saved so that the player returns to their previous state upon finishing the minigame. |
| 1.1.16 | If the player exits the gate with more than 100 tickets a “You Win” message shall pop up for 5 seconds, before closing the game. |
| 1.1.17 | If the player dies in the tent, a “You Lose” message shall appear on screen for 5 seconds before closing the game. |


### Darts (2.1.0)

| ID  | Requirement     | 
| :-------------: | :----------: |
| 2.1.1 | There shall be a dart board. | 
| 2.1.2 | There shall be 15 darts. |
| 2.1.3 | After each throw, the number of darts shall decrease by one. |
| 2.1.4 | The game shall end when the player is out of darts. |
| 2.1.5 | The player shall start will 301 points. |
| 2.1.6 | After each throw, they point value of where the dart landed shall be calculated. | 
| 2.1.7 | After each throw, they point value of where the dart landed shall be subtracted from the total score. |
| 2.1.8 | The game shall end when the total score reaches zero. |
| 2.1.9 | If the point value of a throw would drop the total score below zero, it shall be invalid. |
| 2.1.10 | If the throw is invalid, the total score will not decrease due to the throw.| 
| 2.1.11 | If the throw is invalid, the number of darts will still decrease by one. |
| 2.1.12 | If the dart lands within the outer circle of red and green sections, the point value of the throw shall be tripled. |
| 2.1.13 | If the dart lands within the inner circle of red and green sections, the point value of the throw shall be doubled. |

### Blackjack (3.1.0)

| ID  | Requirement     | 
| :-------------: | :----------: |
| 3.1.1 | There shall be a table surface for the cards to be displayed on | 
| 3.1.2 | The user shall be able to wager their tickets on each game of blackjack | 
| 3.1.3 | Playing cards shall be dealt out to the user and and Dealer to begin the game | 
| 3.1.4 | Players shall have the ability to 'hit', drawing another card |
| 3.1.5 | Players shall have the ability to 'stand' locking in their point total |
| 3.1.6 | The dealer shall be able to determine a winner from both player and dealer hands |
| 3.1.7 | Winnings shall be paid out to the user according to the situation's payout odds | 

### Block Puzzle (4.1.0)

| ID  | Requirement     | 
| :-------------: | :----------: |
| 4.1.1 | The player will be able to move the blocks around the board to play the game. The player can move the blocks left/right and up/down | 
| 4.1.2 | The goal is to move the red block across the board in 20 seconds and secure the most points possible | 
| 4.1.3 | The player will be able to move the blocks in a 2-dimensional format, and not over-lap over other blocks.| 
| 4.1.4 | The player will have 3 tries to secure as many points as possible. |

## Non-Functional Requirements

### Platformer (1.2.0)

| ID  | Requirement     | 
| :-------------: | :----------: | 
| 1.2.1 | The world border shall be represented by a fence so the player can visually see where the play area starts and stops. |
| 1.2.2 | The player controls shall be shown on screen where the player begins the game and where they spawn upon entering the tent. |
| 1.2.3 | There shall be clouds in the background, moving in the same direction and at the same speed, while outside in the carnival area for the world to feel more alive. |
| 1.2.4 | A hint shall appear on screen when the player attempts to exit letting them know what their objectives are. |
| 1.2.5 | A “press ‘e’ to enter” prompt shall display anytime the player is in contact with a minigame booth or the tent. |
| 1.2.6 | The game shall be able to run on both Mac and Windows. |
| 1.2.7 | The player shall be able to close the window and exit the program at any time by pressing the ‘x’ in the top right corner. |

 

### Darts (2.2.0)

| ID  | Requirement     | 
| :-------------: | :----------: | 
| 2.2.1 | The remaining darts shall be displayed on screen. | 
| 2.2.2 | The total score shall be displayed on screen. |
| 2.2.3 | The dart board shall display the point values of the corresponding sections. |

### Blackjack (3.2.0)

| ID  | Requirement     | 
| :-------------: | :----------: | 
| 3.2.1 | The blackjack game shall have a clear card theme to bolster the games clearity usabilty | 
| 3.2.2 | Animations used in the game shall be done modestly to not slow the game down |
| 3.2.3 | Cards dealt shall not cover up other cards preventing the user from seeing what they are |
| 3.2.4 | The placement of the cards on the table should be positioned so it's clear who they belong to |
| 3.2.5 | The users balance shall be updated after each hand so that the user doesn't gamble more than inteneded. |

### Block Puzzle (4.2.0) 

| ID  | Requirement     | 
| :-------------: | :----------: | 
| 4.2.1 | The Block Puzzle game will have 3 tries to win, and each game will last 20 seconds. | 
| 4.2.2 | The goal of the player is to bring the red block to the exit area within 20 seconds |
| 4.2.3 | Each try will have set tickets, with the first attempt being 10 tickets, the second attempt being 7 tickets, and the final attempt being 3 tickets. |
| 4.2.4 | The borders are in bold to show the boundary of the board. |



# Software Artifacts

The first three links(diagrams) were what we used to lay out our initial design and framework for this project. The other three links(Charts and Trello board) are the methods we used in order to keep track of our timeline, progress, and remaining work. 

* [Use-Case Diagram](https://github.com/slomac1/GVSU-CIS350-GVJumpers/blob/main/artifacts/Use%20Case%20Diagram2.pdf)
* [Communication Diagram](https://github.com/slomac1/GVSU-CIS350-GVJumpers/blob/main/artifacts/Communication_Diagram.pdf)
* [Class Diagram](https://github.com/slomac1/GVSU-CIS350-GVJumpers/blob/main/artifacts/Class%20Diagram%20(1).pdf)
* [Gannt Chart](https://github.com/slomac1/GVSU-CIS350-GVJumpers/blob/main/docs/Gantt%20Chart.pdf)
* [Burn-Down Chart](https://github.com/slomac1/GVSU-CIS350-GVJumpers/blob/main/docs/Burn%20Down%20Chart.pdf)
* [Trello Board](https://trello.com/b/qDXeCORB/cis-350-gvjumpers)
