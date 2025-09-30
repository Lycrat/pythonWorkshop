import random
import PersonClass

OPTIONS = ["rock", "paper", "scissor"]

class Game:

    def __init__(self, mode):
        self.player1 = PersonClass.Person('')
        self.player2 = PersonClass.Person('')
        self.mode = mode

    def game_mode_1(self):
        print("Computer vs you")
        self.player2.set_choice(random.choice(OPTIONS))
        while True:
            self.player1.set_choice(input("Enter your choice (Rock, Paper, Scissor): ").lower())
            if self.player1.get_choice() in OPTIONS:
                break

    def game_mode_2(self):
        print("Welcome to a 2 player game")
        while True:
            self.player1.set_choice(input("Player 1 enter your choice (Rock, Paper, Scissor): ").lower())
            if self.player1.get_choice() in OPTIONS:
                break
        while True:
            self.player2.set_choice( input("Player 2 enter your choice (Rock, Paper, Scissor): ").lower())
            if self.player2.get_choice() in OPTIONS:
                break

    def game_logic(self):
        player1_choice = self.player1.get_choice()
        player2_choice = self.player2.get_choice()

        if self.mode == 1:
            self.game_mode_1()
        else:
            self.game_mode_2()

        print(player1_choice, player2_choice)
        if (self.player1.get_choice(), self.player2.get_choice()):
            print("Draw! 🙂‍↔️")
        elif (player1_choice == 'rock' and player2_choice == 'scissor') or (
                player1_choice == 'paper' and player2_choice == 'rock') or (
                player1_choice == 'scissor' and player2_choice == 'paper'):
            print("Player 1 Wins 😆") if self.mode == 2 else print("You win! 🫵🏽🎉")
        else:
            print("Player 2 Wins 🤩") if self.mode == 2 else print("Computer wins! 💪🏽🖥️")