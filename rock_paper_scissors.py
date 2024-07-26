# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

print("Computer chose:" + computer_choice)

# Run Conditionals
#Compare the user's input to the computer's choice to determine if the user won, lost, or tied.
if ((user_choice == "r") and (computer_choice == "s")) or ((user_choice == "s") and (computer_choice == "p")) or ((user_choice == "p") and (computer_choice == "r")):
    print("You beat computer")
elif ((computer_choice == "r") and (user_choice == "s")) or ((computer_choice == "s") and (user_choice == "p")) or ((computer_choice == "p") and (user_choice == "r")):
    print("You lost to computer")
elif ((user_choice == "r") and (computer_choice == "r")) or ((user_choice == "s") and (computer_choice == "s")) or ((user_choice == "p") and (computer_choice == "p")):
    print("Thats a tie between you and computer")
