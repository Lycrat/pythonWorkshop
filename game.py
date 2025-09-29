#Options: single player or multiplayer
#Check how to make terminal invisible

print("Welcome to Rock Paper Scissor!")
option = int(input("Choose 1 for a single-player game or 2 for multiplayer game: "))
print(option)

if (option==1):

elif (option==2):
    # Multiplayer game
    player1_choice = input("Player 1 enter your choice (Rock, Paper, Scissor): ").lower()
    player2_choice = input("Player 2 enter your choice (Rock, Paper, Scissor): ").lower()

    if (player1_choice == "rock") :
        if (player2_choice == 'rock'):
            print("Draw, replay the game")
        elif (player2_choice == 'paper') :
            print("Player 2 wins")
        elif (player2_choice == 'scissor') :
            print("Player 1 wins")
    elif (player1_choice == 'paper'):
        if (player2_choice == 'rock'):
            print("Player 1 wins")
        elif (player2_choice == 'paper') :      
            print("Draw, replay the game")
        elif (player2_choice == 'scissor') :
            print("Player 2 wins")
    elif (player1_choice == 'scissor'):
        if (player2_choice == 'rock'):
            print("Player 2 wins")
        elif (player2_choice == 'paper') :      
            print("Player 1 wins")
        elif (player2_choice == 'scissor') :
            print("Draw, replay the game")
else:

    


