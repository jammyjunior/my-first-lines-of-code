import sys
import random

print("------------------------")
print("Rock Paper Scissors Game")
print("------------------------")
print("Welcome to Rock Paper Scissors Game!")
print("Type 'r' for rock, 'p' for paper, 's' for scissors or 'exit' to exit the program")
userChoice = input("Your choice: ").lower()

# Check if the program cann't be run. userChoice not in acceptAnswer 
userAnswerAccepted = ["rock", "r", "paper", "p", "s", "scissors" "exit"]
while userChoice not in userAnswerAccepted:
    print("Sorry, I can't get it. Try again!")
    print("Type 'r' for rock, 'p' for paper, 's' for scissors or 'exit' to exit the program")
    print()
    userChoice = input("Your choice: ").lower()

# If userChoise in acceptAnswer
# Convert userChoice
if userChoice == "r":
    userChoice = "rock"

elif userChoice == "p":
    userChoice = "paper"

elif userChoice == "s":
    userChoice = "scissors"

#systemChoice
systemList = ["rock", "paper", "scissors"]
systemChoice = random.choice(systemList)

#Result check
resultWin = (userChoice == "rock" and systemChoice == "scissors") or (userChoice == "scissors" and systemChoice == "paper") or (userChoice == "paper" and systemChoice == "rock")
resultLoss = (userChoice == "rock" and systemChoice == "paper") or (userChoice == "paper" and systemChoice == "scissors") or (userChoice == "scissors" and systemChoice == "rock")
resultTie = userChoice == systemChoice

# Print the result
if resultWin == True:
    print("System choice:", systemChoice)
    print()
    print("You won!")

elif resultLoss == True:
    print("System choice:", systemChoice)
    print()
    print("You lose.")

elif resultTie == True:
    print("System choice:", systemChoice)
    print()
    print("It's a tie!")

elif userChoice == "exit":
    print("Exiting...")
    sys.exit(0)

