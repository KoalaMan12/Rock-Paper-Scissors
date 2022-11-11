# Rock paper Scissors has 2 players. For this game
# Player 1 will be the computer. Player 2 is a human
# To make the game fun and usable add the following:
#
#
# 1. Make it so the player can play as many times as they want
# 2. Use a function to determine the winner of the game
# 3. Handle the case where the game ends in a tie
# 4. Check the input to make sure it is one of the 3 choices
#    If it is not, print a message to the screen and let the 
#    Player try again


import random
lost = 0
won = 0
a=random.randint(1,3)
print("Please type Rock, Paper or Scissors")
Player = input()
if a == (1):
  print("Paper")
  if str.lower(Player) == "rock":
    print("You Lose")
  lost += 1
  if str.lower(Player) == "scissors":
      print("You Win")
  won += 1
  if str.lower(Player) == "paper":
      print("You Tied")
if a == (2):
  print("Rock")
  if str.lower(Player) == "scissors":
    print("You Lose")
  if str.lower(Player) == "paper":
      print("You Win")
  if str.lower(Player) == "Rock":
      print("You Tied")
if a == (3):
  print("Scissors")
  if str.lower(Player) == "paper":
    print("You Lose")
  if str.lower(Player) == "rock":
    print("You Win")
  if str.lower(Player) == "scissors":
      print("You Tied")