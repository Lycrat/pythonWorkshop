import random
from GameClass import Game
import getpass

print("Welcome to Rock Paper Scissor!")

while True:
    mode = input("Choose 1 to play against computer or 2 to play against a friend: ")
    if mode == '1' or mode == '2':
        mode = int(mode)
        break

game = None
if (mode==1):
    game = Game(1)
elif (mode==2):
    game = Game(2)
else:
    print('There are only 2 modes, pick 1 or 2')

game.game_logic()



