import random
import getpass
OPTIONS = ["rock", "paper", "scissor"]


def game_logic(player1_choice, player2_choice, mode):
    if(player1_choice == player2_choice):
        print("Draw! 🙂‍↔️")
    elif(player1_choice == 'rock' and player2_choice == 'scissor') or (player1_choice == 'paper' and player2_choice == 'rock') or (player1_choice == 'scissor' and player2_choice == 'paper'):
        print("Player 1 Wins 😆") if mode == 2 else print("You win! 🫵🏽🎉")
    else:
        print("Player 2 Wins 🤩") if mode == 2 else print("Computer wins! 💪🏽🖥️")


print("Welcome to Rock Paper Scissor!")
while True:
    mode = input("Choose 1 to play against computer or 2 to play against a friend: ")
    if mode == '1' or mode == '2':
        mode = int(mode)
        break

if (mode==1):
    print("Computer vs you")
    computer_choice = random.choice(OPTIONS)
    while True:
        player1_choice = input("Enter your choice (Rock, Paper, Scissor): ").lower()
        if player1_choice in OPTIONS:
            break
    game_logic(player1_choice, computer_choice, 1)


elif (mode==2):
    print("Welcome to a 2 player game")
    while True:
        # Use getpass function to conceal player 1 choice
        #player1_choice = getpass.getpass(prompt='Player 1 enter your choice (Rock, Paper, Scissor): ').lower()
        player1_choice = input("Player 1 enter your choice (Rock, Paper, Scissor): ").lower()
        if player1_choice in OPTIONS:
            break
    while True:
        player2_choice = input("Player 2 enter your choice (Rock, Paper, Scissor): ").lower()
        if player2_choice in OPTIONS:
            break
    game_logic(player1_choice, player2_choice, 2)





