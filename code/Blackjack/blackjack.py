# Blackjack minigame main program
import pygame, random, sys, os
import time
from .GUI import BlackjackGUI
from .GUI import Card

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tickets_manager


class GameEngine:
    def __init__(self, balance):
        self.deck = create_deck()
        self.dealer = Dealer()
        self.balance = balance
        self.dealing_done = False
        hand0 = Player("Player") # initialization of 0th index
        self.players = [hand0]  # list of Player objects
        self.current_hand = 0
        self.state = "BETTING"  # Other states: DEALING, PLAYER_TURN, DEALER_TURN, EVALUATE, GAME_OVER

    def update(self, action=None): # state machine
        player: Player = self.players[self.current_hand] # Use player in place of self.players[self.current_hand]

        if self.state == "BETTING":
            # Ask GUI or CLI for bet input, then:
            self.start_round(action) # place bet
            self.state = "DEALING"

        elif self.state == "DEALING":
            self.deal_initial_cards()
            self.state = "DEALT"

        elif self.state == "DEALT":
            if self.check_blackjack():
                self.state = "DEALER_SHOW"
            else:
                self.state = "PLAYER_TURN"

        elif self.state == "PLAYER_TURN":
            if action == "hit":
                self.hit()
                self.state = "ADDING_CARD"
                # doesn't immediately advance state
                
            elif action == "stand":
                self.next_hand_or_dealer()
            elif action == "double":
                self.double_down()
                # Advances after 1 card draw
                self.next_hand_or_dealer()
            elif action == "split":
                self.split_hand()
        
        elif self.state == "ADDING_CARD":
            if player.score > 21: # check for player bust
                self.next_hand_or_dealer() # advance turn to split hand or dealer
            self.state = "PLAYER_TURN"

        elif self.state == "DEALER_SHOW":
            self.state = "DEALER_TURN"

        elif self.state == "DEALER_TURN":
            self.draw()

        elif self.state == "DEALER_DRAW":
            if get_score(self.dealer.hand) >= 17:
                self.state = "EVALUATE"
            else:
                self.state = "DEALER_TURN"

        elif self.state == "EVALUATE":
            for hand in self.players:
                self.determine_winner()
            # self.state = "GAME_OVER"

        elif self.state == "WINNER":
            # Win, Prize, play again, quit
            pass

        elif self.state == "LOSER":
            # Loss, play again, quit
            pass


        elif self.state == "GAME_OVER":
            self.reset_round()
            self.state = "BETTING"
    
    def get_valid_actions(self):
        if self.state == "PLAYER_TURN":
            actions = ['hit', 'stand']
            if self.can_double():
                actions.append('double')
            if self.can_split():
                actions.append('split')
            return actions
        elif self.state == "BETTING":
            return ['bet', 'Quit', 'exit']
        elif self.state == "EVALUATING":
            return []
        else:
            return []

    def can_double(self):
        return (
            len(self.curr_player().hand) == 2 and 
            self.balance >= self.curr_player().bet
        )

    def can_split(self):
        hand = self.curr_player().hand
        return (
            len(hand) == 2 and 
            hand[0][0] == hand[1][0] and  # [card][0 (rank)]
            self.balance >= self.curr_player().bet
        )

    def next_hand_or_dealer(self):
        if self.current_hand + 1 < len(self.players):
            self.current_hand += 1
        else:
            self.state = "DEALER_SHOW"

    def split_hand(self):
        player: Player = self.players[self.current_hand]
        card1, card2 = player.hand
        bet = player.bet
        
        if self.balance < bet:
            return
        # Deduct second bet from balance
        self.balance -= bet

        # Create new player hands
        hand1 = Player(name="Hand 1")
        hand1.hand = [card1]
        hand1.bet = bet
        hand1.score = get_score(hand1.hand)

        hand2 = Player(name="Hand 2")
        hand2.hand = [card2]
        hand2.bet = bet
        hand2.score = get_score(hand2.hand)

        # Replace current hand with hand1, add hand2 after
        self.players[self.current_hand] = hand1
        self.players.insert(self.current_hand + 1, hand2)

    def double_down(self):
        # Logic to double bet and hit once
        self.balance = self.balance - self.curr_player().bet # update balance
        self.curr_player().bet = self.curr_player().bet * 2 # double the bet
        self.hit()
        
    def hit(self):
        # Add one card to player
        self.curr_player().add_card(self.deck.pop(0))
        self.curr_player().score = get_score(self.curr_player().hand) # update player score
        display_hand(self.curr_player())

    def draw(self):
        # draw until 17 reached or bust
        display_hand(self) # show 2nd card
        if get_score(self.dealer.hand) > 17:
            self.state = "EVALUATE"
        
        self.dealer.add_card(self.deck.pop(0))
        self.state = "DEALER_DRAW"
    

    def start_round(self, bet_amount):
        if self.balance < bet_amount:
            return

        self.balance -= bet_amount

        # player_hand = Player(name="Player")
        # player_hand.bet = bet_amount
        self.curr_player().bet = bet_amount
        # self.players.append(player_hand)

        self.dealer.reset()
    
    def curr_player(self):
        return self.players[self.current_hand]

    def deal_initial_cards(self):
        # Deal 2 cards to player(s) and dealer

        # Player 1st card
        self.curr_player().add_card(self.deck.pop(0))
        display_hand(self.curr_player()) # print 1st player card

        # Dealer 1st card
        self.dealer.add_card(self.deck.pop(0))
        display_hand(self.dealer) # print 1st dealer card
        
        # Player 2nd card
        self.curr_player().add_card(self.deck.pop(0))
        display_hand(self.curr_player())

        # Dealer 2nd card
        self.dealer.add_card(self.deck.pop(0))
        # self.dealing_done = True
        
    def check_blackjack(self):
        # Check if player or dealer has blackjack
        # check for player blackjack
        if get_score(self.curr_player().hand) == 21:
            display_hand(self.dealer) # show dealer 2nd card
            return True

        # check for dealer blackjack
        elif get_score(self.dealer.hand) == 21:
            display_hand(self.dealer) # print dealer 2nd card
            # self.determine_winner()
            return True
        
        return False
    
    def determine_winner(self):
        player: Player = self.players[self.current_hand]
        # Special Case: Player Blackjack!
        if len(player.hand) == 2 and get_score(player.hand) == 21:
            self.balance += (2*player.bet+.5*player.bet)
            self.state = "WINNER"
        # Dealer busts
        elif get_score(self.dealer.hand) > 21:
            self.balance += (2*player.bet)
            self.state = "WINNER"
        # Player busts
        elif get_score(player.hand) > 21:
            self.state = "LOSER"
        # Dealer wins, no player bust
        elif get_score(self.dealer.hand) > get_score(player.hand):
            self.state = "LOSER"
        # Push
        elif get_score(self.dealer.hand) == get_score(player.hand):
            self.balance += player.bet
            self.state = "WINNER"

        # Player Wins, no dealer bust
        elif get_score(self.dealer.hand) < get_score(player.hand):
            self.balance += (2*player.bet)
            self.state = "WINNER"
        else:
            self.state = "GAME_OVER"
        
    def reset_round(self):
        self.deck = create_deck()
        hand0 = Player("Player")
        self.players = [hand0] # keeps list index 0 in range
        self.current_hand = 0
        self.dealing_done = False
        self.dealer.reset()


class Dealer:
    def __init__(self, name="Dealer"):
        self.name = name
        self.hand = []
        self.score = 0

    def __str__(self):
        # prints last card drawn by the Player and new total
        cards = ', '.join(str(card) for card in self.hand)
        return f"{self.name} Hand: {cards} | Total: {self.score}"
        

    def add_card(self, card):
        self.hand.append(card)
        self.score = get_score(self.hand) # update hand score
    
    def reset(self):
        self.hand = []
        self.score = 0

class Player: # Repersents individual hand
    def __init__(self, name="Player"):
        self.name = name
        self.hand = []
        self.bet = 0
        self.score = 0
        self.standing = False

    def __str__(self):
        # prints last card drawn by the Player and new total
        cards = ', '.join(str(card) for card in self.hand)
        return f"{self.name} Hand: {cards} | Total: {self.score}"

    def add_card(self, card):
        self.hand.append(card)
        self.score = get_score(self.hand) # update hand score

    def reset(self):
        self.hand = []
        self.score = 0
        self.bet = 0
        self.standing = False
    

# Define your classes or functions here
def get_score(hand):
        total = 0
        aces = 0
        for card in hand:
            rank = card[0] # format: [('A', 'spades')]
            if rank in ['J', 'Q', 'K']:
                total += 10
            elif rank == 'A':
                total += 11
                aces += 1
            else:
                total += int(rank)
        # Adjust for Aces
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

def create_deck():
    # Returns a shuffled deck
    suits = ['spades', 'hearts', 'clubs', 'diamonds']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']
    deck = []

    # create deck of (suit, value) cards
    for suit in suits:
        for value in values:
            card = (value, suit)
            deck.append(card)
    game_deck = deck*3
    random.shuffle(game_deck)

    return game_deck

def display_hand(hand):
    print(hand) # prints either Player or Dealer str method

def get_user_input(valid):
    while True:
        action = input("> ").strip().lower()

        if "bet" in valid:
            # Expecting a number input for a bet

            if action.isdigit() and int(action) > 0:
                return int(action)
            elif action.strip().lower() == 'exit':
                return action
            else:
                print("Please enter a valid positive number for your bet.")
        else:
            # Expecting a string input (hit, stand, etc.)
            if action in valid:
                return action
            else:
                print(f"Invalid action. Please choose one of: {', '.join(valid)}")


# Constants
CARD_WIDTH = 100
CARD_HEIGHT = 150
FPS = 60
WIDTH, HEIGHT = 800, 600
GREEN = (34, 139, 34)

def play_game_gui():
    
    # Set up display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blackjack Table")

    pygame.init()
    clock = pygame.time.Clock()
    gui = BlackjackGUI(screen)
    engine = GameEngine(tickets_manager.load_tickets())

    clock = pygame.time.Clock()
    running = True
    waiting_for_action = True
    action_to_apply = None

    while running:
        gui.draw(engine)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                break

        # Pass events to GUI to see if a user action occurred
        gui.handle_events(events)

        # Get the current valid actions from game state
        valid_actions = engine.get_valid_actions()

        # Handle game states that need user interaction
        if engine.state == "BETTING":
            # gui.show_input_box = True
            gui.show_buttons("Quit", "Deal")
            if gui.bet_entered is not None:
                action_to_apply = gui.bet_entered
                gui.bet_entered = None
                waiting_for_action = False
            # Quit button pressed    
            elif gui.last_button_pressed in valid_actions:
                action_to_apply = gui.last_button_pressed
                gui.last_button_pressed = None
                waiting_for_action = False

        elif engine.state == "DEALING" :
            # deal cards animation
            gui.hide_all_buttons()
            waiting_for_action = False

        elif engine.state == "DEALT":
            if len(engine.curr_player().hand) >= 2 and len(engine.dealer.hand) >= 2:
                rank, suit = card_image(engine.curr_player().hand[0])
                p1 = Card(rank, suit)
                rank, suit = card_image(engine.dealer.hand[0])
                d1 = Card(rank, suit)
                rank, suit = card_image(engine.curr_player().hand[1])
                p2 = Card(rank, suit)
                rank, suit = card_image(engine.dealer.hand[1])
                d2 = Card(rank, suit)
                gui.animate_card_flip(p1, 300, 400, engine, face_up=True)
                gui.animate_card_flip(d1, 250, 50, engine, face_up=True)
                gui.animate_card_flip(p2, 340, 380, engine, face_up=True)
                gui.animate_card_flip(d2, 360, 50, engine, face_up=False)

            gui.hide_all_buttons()
            waiting_for_action = False
            
        elif engine.state == "PLAYER_TURN":
            # looping animations were here
            gui.show_buttons("hit", "stand", "double", "split")
            if gui.last_button_pressed in ['hit', 'stand', 'Hit', 'Stand']:
                action_to_apply = gui.last_button_pressed
                gui.last_button_pressed = None
                waiting_for_action = False
        
        elif engine.state == "ADDING_CARD":
            # card animation
            card_num = len(engine.curr_player().hand)
            rank, suit = card_image(engine.curr_player().hand[card_num-1])
            x_coor, y_coor = hit_position(card_num)
            p3 = Card(rank, suit)
            gui.animate_card_flip(p3, x_coor, y_coor, engine, face_up=True)
            gui.hide_all_buttons()
            waiting_for_action = False

        elif engine.state == "DEALER_SHOW":
            gui.animate_card_flip(d2, 360, 50, engine, face_up=True)
            gui.hide_all_buttons()
            waiting_for_action = False
        
        elif engine.state == "DEALER_DRAW":
            # card animation
            card_num = len(engine.dealer.hand)
            rank, suit = card_image(engine.dealer.hand[card_num-1])
            x_coor, y_coor = d_hit_position(card_num)
            d3 = Card(rank, suit)
            gui.animate_card_flip(d3, x_coor, y_coor, engine, face_up=True)
            gui.hide_all_buttons()
            waiting_for_action = False
        
        elif engine.state == "WINNER":
            winner_msg = f"You win!! {2*engine.curr_player().bet} Credits!"
            gui.draw_popup(winner_msg)
            gui.show_buttons("Continue")
            gui.draw(engine)  # redraw all elements
            gui.draw_popup(winner_msg)  # then draw popup on top
            if gui.last_button_pressed == "Continue":
                gui.last_button_pressed = None
                gui.persistent_cards.clear()
                engine.reset_round()  
                engine.state = "BETTING"

        elif engine.state == "LOSER":
            gui.draw_popup("You Lose:(")
            gui.show_buttons("Continue")
            gui.draw(engine)  # redraw all elements
            gui.draw_popup("You Lose:(")  # then draw popup on top
            if gui.last_button_pressed == "Continue":
                gui.last_button_pressed = None
                gui.persistent_cards.clear()
                engine.reset_round()  
                engine.state = "BETTING"
        
        else:
            gui.hide_all_buttons()
            waiting_for_action = False  # Auto progress for non-input states

        gui.last_button_pressed = None

        # If we received an action (bet or gameplay move), apply it
        if not waiting_for_action:
            engine.update(action_to_apply)
            action_to_apply = None
            waiting_for_action = True

        # Check if the game is over
        if engine.balance <= 0 or engine.state == "GAME_OVER":
            running = False

        clock.tick(60)
    tickets_manager.save_tickets(engine.balance)
    pygame.quit()

def hit_position(card_num):
    x = card_num*40 + 260
    y = card_num*-20 + 420
    return x, y

def d_hit_position(card_num):
    x = card_num*110+140
    y = 50
    return x, y

def card_image(card):
    if card[0] == 'J':
        rank = '11'
    elif card[0] == 'Q':
        rank = '12'
    elif card[0] == 'K':
        rank = 13
    elif card[0] == 'A':
        rank = 1
    else:
        rank = card[0]
    if card[1] == 'spades':
        suit = 'S'
    elif card[1] == 'clubs':
        suit = 'C'
    elif card[1] == 'hearts':
        suit = 'H'
    else:
        suit = 'D'

    return rank, suit

def play_game():
    engine = GameEngine(balance=10)
    end = False
    while engine.balance > 0 and end is False:
        valid = engine.get_valid_actions()
        
        # Only ask for input if there is something valid to input
        if valid:
            action = get_user_input(valid)
            if action == "exit":
                break
            engine.update(action)
        else:
            engine.update()  # No user input needed, just advance the state

