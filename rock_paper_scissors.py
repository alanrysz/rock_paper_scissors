#Write your code below this line 👇
import random
import art

options = [rock, paper, scissors]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

computerChoice = random.randint(0,2)

if(userChoice >= 3 or userChoice < 0):
  print("You put an invalid number, you lose!")
else:
  print("\nYou choose:\n " + options[opt])
  print("The IA choose:\n " + options[randomOpt])


  if(userChoice == 0 and computerChoice == 2):
    print("You Win")
  elif(computerChoice == 0 and userChoice == 2):
    print("You lose")
  elif(computerChoice > userChoice):
    print("You lose")
  elif(userChoice > computerChoice):
    print("You Win")
  elif(userChoice == computerChoice):
    print("Draw")
