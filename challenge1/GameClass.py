import random

OPTIONS = ["rock", "paper", "scissor"]

class Game:

    def __init__(self, mode):
        self.player1_choice = ''
        self.player2_choice = ''
        self.mode = mode

    def game_mode_1(self):
        print("Computer vs you")
        self.player2_choice = random.choice(OPTIONS)
        while True:
            self.player1_choice = input("Enter your choice (Rock, Paper, Scissor): ").lower()
            if self.player1_choice in OPTIONS:
                break

    def game_mode_2(self):
        print("Welcome to a 2 player game")
        while True:
            # Use getpass function to conceal player 1 choice
            # player1_choice = getpass.getpass(prompt='Player 1 enter your choice (Rock, Paper, Scissor): ').lower()
            self.player1_choice = input("Player 1 enter your choice (Rock, Paper, Scissor): ").lower()
            if self.player1_choice in OPTIONS:
                break
        while True:
            self.player2_choice = input("Player 2 enter your choice (Rock, Paper, Scissor): ").lower()
            if self.player2_choice in OPTIONS:
                break

    def game_logic(self):
        if self.mode == 1:
            self.game_mode_1()
        else:
            self.game_mode_2()
        if (self.player1_choice == self.player2_choice):
            print("Draw! 🙂‍↔️")
        elif (self.player1_choice == 'rock' and self.player2_choice == 'scissor') or (
                self.player1_choice == 'paper' and self.player2_choice == 'rock') or (
                self.player1_choice == 'scissor' and self.player2_choice == 'paper'):
            print("Player 1 Wins 😆") if self.mode == 2 else print("You win! 🫵🏽🎉")
        else:
            print("Player 2 Wins 🤩") if self.mode == 2 else print("Computer wins! 💪🏽🖥️")