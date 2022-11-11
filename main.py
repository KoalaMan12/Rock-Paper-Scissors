import random
a=random.randint(1,3)
print("Please type Rock, Paper or Scissors")
Player = input()
if a == (1):
  print("Paper")
  if str.lower(Player) == "rock":
    print("You Lose")
  if str.lower(Player) == "scissors":
      print("You Win")

if a == (2):
  print("Rock")
  if str.lower(Player) == "scissors":
    print("You Lose")
  if str.lower(Player) == "paper":
      print("You Win")

if a == (3):
  print("Scissors")
  if str.lower(Player) == "paper":
    print("You Lose")
  if str.lower(Player) == "rock":
    print("You Win")
    print()
